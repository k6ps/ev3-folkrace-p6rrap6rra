import ev3dev.ev3 as ev3
import logging

INITIALIZE_EXPERIMENTAL_TURN_MAX_CYCLE_COUNT = 100
INITIALIZE_EXPERIMENTAL_TURN_SLEEP_BETWEEN_CYCLES_MILLISEC = 100
INITIALIZE_EXPERIMENTAL_TURN_POSITION_SP = -5
INITIALIZE_EXPERIMENTAL_TURN_MAX_POSITION_HAS_NOT_CHANGED_CYCLE_COUNT = 5


class Steering(object):

    def __init__(self, steering_motor_address, steering_motor_speed_factor, steering_speed, steering_max_range, steering_motor_position_factor):
        self.steering_motor_speed_factor = steering_motor_speed_factor
        self.steering_speed = steering_speed
        self.steering_max_range = steering_max_range
        self.steering_motor_position_factor = steering_motor_position_factor
        self.steering_motor = ev3.MediumMotor(steering_motor_address)
        self.steering_motor_speed = self.steering_speed * self.steering_motor_speed_factor

    def __experimentally_find_max_left_position(self):
        __previous_position = self.steering_motor.position
        __position_has_not_changed_counter = 0
        for i in range(0, INITIALIZE_EXPERIMENTAL_TURN_MAX_CYCLE_COUNT):
            self.steering_motor.run_to_rel_pos(
                position_sp=(self.steering_motor_position_factor * INITIALIZE_EXPERIMENTAL_TURN_POSITION_SP),
                speed_sp=self.steering_motor_speed,
                stop_action='hold'
            )
            self.steering_motor.wait_while('running', timeout=INITIALIZE_EXPERIMENTAL_TURN_SLEEP_BETWEEN_CYCLES_MILLISEC)
            self.steering_motor.stop(stop_action='hold')
            if (__previous_position == self.steering_motor.position):
                __position_has_not_changed_counter = __position_has_not_changed_counter + 1
            else:
                __position_has_not_changed_counter = 0
            __previous_position = self.steering_motor.position
            if (__position_has_not_changed_counter >= INITIALIZE_EXPERIMENTAL_TURN_MAX_POSITION_HAS_NOT_CHANGED_CYCLE_COUNT):
                break
        self.steering_motor.stop(stop_action='hold')

    def initialize(self):
        logging.debug('Steering: initialize: beginning steering motor position = '+ str(self.steering_motor.position))
        self.__experimentally_find_max_left_position()
        logging.debug('Steering: initialize: steering motor position after experimentally turning max left = '+ str(self.steering_motor.position))
        self.steering_motor.run_to_rel_pos(
            position_sp=(self.steering_motor_position_factor * self.steering_max_range),
            speed_sp=self.steering_motor_speed,
            stop_action='coast'
        )
        self.steering_motor.wait_while('running', timeout=1000)
        self.steering_motor.stop(stop_action='coast')
        logging.debug('Steering: initialize: ending steering motor position = '+ str(self.steering_motor.position))
        self.steering_motor.reset()
        logging.debug('Steering: initialize: steering motor position after reset = '+ str(self.steering_motor.position))

    def get_current_steering_position(self):
        logging.debug('Steering: get_current_steering_position: steering motor position = '+ str(self.steering_motor.position))
        __current_steering_position = self.steering_motor_position_factor * int(self.steering_motor.position * 100 / self.steering_max_range)
        logging.debug('Steering: get_current_steering_position: steering position = '+ str(__current_steering_position))
        return __current_steering_position

    def set_steering_position(self, desired_steering_position):
        logging.debug('Steering: set_steering_position: desired_steering_position = ' + str(desired_steering_position))
        logging.debug('Steering: set_steering_position: steering motor position = ' + str(self.steering_motor.position))
        __desired_steering = self.steering_motor_position_factor * int(desired_steering_position * self.steering_max_range / 100)
        logging.debug('Steering: set_steering_position: desired_steering = ' + str(__desired_steering))
        self.steering_motor.run_to_abs_pos(
            position_sp=__desired_steering,
            speed_sp=self.steering_motor_speed,
            stop_action='coast'
        )
