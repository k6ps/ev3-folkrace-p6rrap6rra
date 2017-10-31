import ev3dev.ev3 as ev3

class Engine(object):

    def __init__(self):
        self.motor_1 = ev3.LargeMotor('outB')
        self.motor_2 = ev3.LargeMotor('outC')

    def setSpeed(self, speed):
        self.motor_1.run_forever(speed_sp=-1000)
        self.motor_2.run_forever(speed_sp=-1000)

