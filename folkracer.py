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
        self._stop_requested = False
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
        time_frame_length_seconds = 0.001 * self.settings.getTimeFrameMilliseconds()
        while (self._stop_requested == False):
            if (State.RUNNING == self.getState()):
                self._performRunningCycle()
            time.sleep(time_frame_length_seconds)
        logging.debug('Folkracer stopped')

    def getState(self):
        return self.state

    def startButtonPressed(self):
        self.enterStartingState()

    def stop(self):
        self._stop_requested == True

    def _performRunningCycle(self):
        bumper_statuses = self.bumpers.getBumperStatuses()
        distances = self.distances.getDistances()
        logging.debug('distances = ' + str(distances))
        desired_steering = self.calculate_desired_steering(distances)
        logging.debug('desired steering = ' + str(desired_steering))
        self.steering.setSteeringPosition(round(desired_steering, 2))
        self.engine.setSpeed(100)

    def calculate_desired_steering(self, distances):
        left_ = distances['left']
        right_ = distances['right']
        if (left_ < right_):
            steering = (right_ * 100 / left_) - 100
        elif (left_ > right_):
            steering = -1 * ((left_ * 100 / right_) - 100)
        else:
            steering = 0.0
        return steering

class ExpectedSteeringCalculator(object):

    def __init__(self, max_side_distance, norm_side_distance, min_side_distance, max_steering_error):
        self.max_side_distance = max_side_distance
        self.norm_side_distance = norm_side_distance
        self.min_side_distance = min_side_distance
        self.max_steering_error = max_steering_error

    def calculateExpectedSteering(self, left_distance, right_distance):
        if (left_distance < self.min_side_distance and right_distance > self.min_side_distance):
            steering_error = self.max_steering_error
        elif (right_distance < self.min_side_distance and left_distance > self.min_side_distance):
            steering_error = -self.max_steering_error
        elif (right_distance > self.max_side_distance and left_distance > self.max_side_distance):
            steering_error = 0
        elif (right_distance > self.max_side_distance):
            steering_error = self.norm_side_distance - left_distance
        elif (left_distance > self.max_side_distance):
            steering_error = right_distance - self.norm_side_distance
        else:
            steering_error = right_distance - left_distance
        return int((steering_error) * 100 / self.max_steering_error)



