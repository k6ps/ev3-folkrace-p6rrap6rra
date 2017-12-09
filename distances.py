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
            'right':int(self.distance_sensor_right.value() * 0.1),
            'left':int(self.distance_sensor_left.value() * 0.1)
        }
        if (self.distance_sensor_front is not None):
            distances['front'] = int(self.distance_sensor_front.value() * 0.1)
        return distances