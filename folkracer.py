import time
import logging
from enum import Enum
from threading import Thread


class State(Enum):
    AWAITING_START = 0
    STARTING = 1
    RUNNING = 2


class StartDelaySecondsRunner(Thread):

    def __init__(self, folkracer):
        Thread.__init__(self)
        self.folkracer = folkracer

    def run(self):
        start_delay_seconds = self.folkracer.settings.getStartDelaySeconds()
        for _ in range(0, start_delay_seconds):
            time.sleep(1)
            self.folkracer.lights_and_sounds.startDelaySecond()
        self.folkracer.enterRunningState()


class Folkracer(Thread):

    def __init__(self, steering, engine, distances, bumpers, buttons, settings, orientation, log, lights_and_sounds):
        Thread.__init__(self)
        self.steering = steering
        self.steering.initialize()
        self.engine = engine
        self.distances = distances
        self.bumpers = bumpers
        self.buttons = buttons
        self.settings = settings
        self.orientation = orientation
        self.log = log
        self.lights_and_sounds = lights_and_sounds
        self.expected_steering_calculator = ExpectedSteeringCalculator(
            self.settings.getMaxSideDistance(),
            self.settings.getNormSideDistance(),
            self.settings.getMinSideDistance(),
            self.settings.getMaxSteeringError()
        )
        self.stop_requested = False
        self.setDaemon(True)
        self.enterAwaitingStartState()

    def enterAwaitingStartState(self):
        logging.debug('Entering AWAITING_START state')
        self.state = State.AWAITING_START
        self.buttons.start()
        self.buttons.addStartButtonListener(self)

    def enterRunningState(self):
        logging.debug('Entering RUNNING state')
        self.state = State.RUNNING

    def enterStartingState(self):
        logging.debug('Entering STARTING state')
        self.state = State.STARTING
        self.buttons.removeStartButtonListener()
        StartDelaySecondsRunner(self).start()

    def run(self):
        logging.debug('Folkracer started')
        __time_frame_length_seconds = 0.001 * self.settings.getTimeFrameMilliseconds()
        while (self.stop_requested == False):
            if (State.RUNNING == self.getState()):
                self.__perform_running_cycle()
            time.sleep(__time_frame_length_seconds)
        logging.debug('Folkracer stopped')

    def getState(self):
        return self.state

    def startButtonPressed(self):
        self.enterStartingState()

    def stop(self):
        self.stop_requested == True

    def __perform_running_cycle(self):
        __bumper_statuses = self.bumpers.getBumperStatuses()
        __distances = self.distances.getDistances()
        logging.debug('distances = ' + str(__distances))
        __desired_steering = int(self.__calculate_desired_steering(__distances))
        logging.debug('desired steering = ' + str(__desired_steering))
        self.steering.set_steering_position(__desired_steering)
        self.engine.setSpeed(100)

    def __calculate_desired_steering(self, distances):
        __expected_steering = self.expected_steering_calculator.calculate_expected_steering(
            distances['left'],
            distances['right']
        )
        logging.debug('expected steering = ' + str(__expected_steering))
        __actual_steering = self.steering.get_current_steering_position()
        logging.debug('actual steering = ' + str(__actual_steering))

        return __expected_steering


class ExpectedSteeringCalculator(object):

    def __init__(self, max_side_distance, norm_side_distance, min_side_distance, max_steering_error):
        self.max_side_distance = max_side_distance
        self.norm_side_distance = norm_side_distance
        self.min_side_distance = min_side_distance
        self.max_steering_error = max_steering_error

    def calculate_expected_steering(self, left_distance, right_distance):
        if (left_distance < self.min_side_distance and right_distance > self.min_side_distance):
            __expected_steering = self.max_steering_error
        elif (right_distance < self.min_side_distance and left_distance > self.min_side_distance):
            __expected_steering = -self.max_steering_error
        elif (right_distance > self.max_side_distance and left_distance > self.max_side_distance):
            __expected_steering = 0
        elif (right_distance > self.max_side_distance):
            __expected_steering = self.norm_side_distance - left_distance
        elif (left_distance > self.max_side_distance):
            __expected_steering = right_distance - self.norm_side_distance
        else:
            __expected_steering = right_distance - left_distance
        return int((__expected_steering) * 100 / self.max_steering_error)


class SteeringPIDCalculator(object):

    def __init__(self):
        self.proportional_gain = 1.2
        self.integral_gain = 1.0
        self.derivative_gain = 0.001
        self.integral_term_limit = 20.0
        self.proportional_term = 0.0
        self.integral_term = 0.0
        self.derivative_term = 0.0
        self.last_error = 0.0
        self.current_time = time.time()
        self.last_time = self.current_time
        self.set_point = 0.0

    def set_set_point(self, set_point):
        self.set_point = set_point

    def reset(self):
        self.proportional_term = 0.0
        self.integral_term = 0.0
        self.derivative_term = 0.0
        self.last_error = 0.0
        self.current_time = time.time()
        self.last_time = self.current_time
        self.set_point = 0.0

    def calculate(self, feedback_value):
        __error = self.set_point - feedback_value

        self.current_time = time.time()
        __delta_time = self.current_time - self.last_time
        __delta_error = __error - self.last_error

        self.proportional_term = self.proportional_gain * __error
        self.integral_term += __error * __delta_time

        if (self.integral_term < -self.integral_term_limit):
            self.integral_term = -self.integral_term_limit
        elif (self.integral_term > self.integral_term_limit):
            self.integral_term = self.integral_term_limit

        self.derivative_term = 0.0
        if (__delta_time > 0):
            self.derivative_term = __delta_error / __delta_time

        self.last_time = self.current_time
        self.last_error = __error

        return self.proportional_term + (self.integral_gain * self.integral_term) + (self.derivative_gain * self.derivative_term)
