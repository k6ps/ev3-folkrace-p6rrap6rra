import ev3dev.ev3 as ev3
import logging

class Steering:

    def __init__(self, settings):
        self.steering_motor = ev3.MediumMotor(settings.getSteeringMotorAddress())
        self.steering_motor_speed_factor = settings.getSteeringMotorSpeedFactor()
        self.steering_speed = settings.getSteeringSpeed()
        self.steering_max_range = settings.getSteeringMaxRange()

    def initialize(self):
        _steering_speed = self.steering_speed * self.steering_motor_speed_factor
        logging.debug('Steering motor position = '+ str(self.steering_motor.position_sp))
        self.steering_motor.run_to_rel_pos(position_sp=20, speed_sp=_steering_speed, stop_action="hold")
        logging.debug('Steering motor position = '+ str(self.steering_motor.position_sp))
