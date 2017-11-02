import ev3dev.ev3 as ev3

class Steering:

    def __init__(self, settings):
        self.steering_motor = ev3.MediumMotor(settings.getSteeringMotorAddress())

    def initialize(self):
        return
