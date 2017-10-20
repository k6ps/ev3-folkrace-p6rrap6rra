import ev3dev.ev3 as ev3
from ev3dev.core import *

class Distances(object):

    def __init__(self):
        self.distance_sensor_right = UltrasonicSensor('in1')

    def start(self):
        pass

    def getDistances(self):
        return self.distance_sensor_right.value()
