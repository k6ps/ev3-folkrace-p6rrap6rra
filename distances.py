import ev3dev.ev3 as ev3


class Distances(object):

    def __init__(self, settings):
        self.distance_sensor_right = ev3.UltrasonicSensor(settings.getRightDistanceSensorAddress())
        self.distance_sensor_left = ev3.UltrasonicSensor(settings.getLeftDistanceSensorAddress())
        if (settings.hasFrontDistanceSensor()):
           self.distance_sensor_front = ev3.UltrasonicSensor(settings.getFrontDistanceSensorAddress())
        else:
           self.distance_sensor_front = None

    def getDistances(self):
        distances = {
            'right':self.distance_sensor_right.value(),
            'left':self.distance_sensor_left.value()
        }
        if (self.distance_sensor_front is not None):
            distances['front'] = self.distance_sensor_front.value()
        return distances