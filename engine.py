import ev3dev.ev3 as ev3


class Engine(object):

    def __init__(self, settings):
        self.motor_1 = ev3.LargeMotor(settings.getMotor1Address())
        self.motor_2 = ev3.LargeMotor(settings.getMotor2Address())
        self.speed_factor = settings.getMotorSpeedFactor()

    def setSpeed(self, speed):
        _speed = speed * self.speed_factor
        self.motor_1.run_forever(speed_sp = _speed)
        self.motor_2.run_forever(speed_sp = _speed)

    def stop(self):
        self.motor_1.stop(stop_action="coast")
        self.motor_2.stop(stop_action="coast")
        self.motor_1.reset()
        self.motor_2.reset()

    def brake(self):
        self.motor_1.stop(stop_action="brake")
        self.motor_2.stop(stop_action="brake")
        self.motor_1.reset()
        self.motor_2.reset()

