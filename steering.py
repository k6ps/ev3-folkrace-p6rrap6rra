import ev3dev.ev3 as ev3
import logging
import time

STEERING_POSITION_ROUND_DECIMAL_PLACES = 2

INITIALIZE_EXPERIMENTAL_TURN_MAX_CYCLE_COUNT = 100
INITIALIZE_EXPERIMENTAL_TURN_SLEEP_BETWEEN_CYCLES_SEC = 0.1
INITIALIZE_EXPERIMENTAL_TURN_POSITION_SP = 5
INITIALIZE_EXPERIMENTAL_TURN_MAX_POSITION_HAS_NOT_CHANGED_CYCLE_COUNT = 5
INITIALIZE_RETURN_TO_CENTER_COMPENSATE_POSITION_SP = 7

class Steering:

    def __init__(self, settings):
        self.steering_motor = ev3.MediumMotor(settings.getSteeringMotorAddress())
        self.steering_motor_speed_factor = settings.getSteeringMotorSpeedFactor()
        self.steering_speed = settings.getSteeringSpeed()
        self.steering_max_range = settings.getSteeringMaxRange()

    def initialize(self):
        _steering_speed = self.steering_speed * self.steering_motor_speed_factor
        logging.debug('initialize: beginning steering motor position = '+ str(self.steering_motor.position))
        self._experimentallyFindMaxLeftPosition(_steering_speed)
        logging.debug('initialize: steering motor position after experimentally turning max left = '+ str(self.steering_motor.position))
        self.steering_motor.run_to_rel_pos(position_sp=-(self.steering_max_range + INITIALIZE_RETURN_TO_CENTER_COMPENSATE_POSITION_SP), speed_sp=_steering_speed, stop_action='hold')
        time.sleep(1)
        logging.debug('initialize: ending steering motor position = '+ str(self.steering_motor.position))
        self.steering_motor.position = 0

    def _experimentallyFindMaxLeftPosition(self, _steering_speed):
        _previous_position = self.steering_motor.position
        _position_has_not_changed_counter = 0
        for i in range(0, INITIALIZE_EXPERIMENTAL_TURN_MAX_CYCLE_COUNT):
            self.steering_motor.run_to_rel_pos(position_sp=INITIALIZE_EXPERIMENTAL_TURN_POSITION_SP, speed_sp=_steering_speed, stop_action='hold')
            time.sleep(INITIALIZE_EXPERIMENTAL_TURN_SLEEP_BETWEEN_CYCLES_SEC)
            if (_previous_position == self.steering_motor.position):
                _position_has_not_changed_counter = _position_has_not_changed_counter + 1
            else:
                _position_has_not_changed_counter = 0
            _previous_position = self.steering_motor.position
            if (_position_has_not_changed_counter >= INITIALIZE_EXPERIMENTAL_TURN_MAX_POSITION_HAS_NOT_CHANGED_CYCLE_COUNT):
                break

    def getCurrentSteeringPosition(self):
        logging.debug('getCurrentSteeringPosition: steering motor position = '+ str(self.steering_motor.position))
        _current_steering_position = (self.steering_motor.position * 100 / self.steering_max_range)
        _rounded_current_steering_position = round(_current_steering_position, STEERING_POSITION_ROUND_DECIMAL_PLACES)
        logging.debug('getCurrentSteeringPosition: rounded steering position = '+ str(_rounded_current_steering_position))
        return _rounded_current_steering_position

    def setSteeringPosition(self, steering):
        logging.debug('setSteeringPosition: ' + str(steering))
