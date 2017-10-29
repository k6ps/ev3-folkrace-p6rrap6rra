#/usr/bin/python3

import ev3dev.ev3 as ev3
import logging
from folkracer import Folkracer
from steering import Steering
from buttons import Buttons
from distances import Distances
from lights_and_sounds import LightsAndSounds

logging.basicConfig(format='%(asctime)s %(message)s', filename='folkracer.log', level=logging.DEBUG)

class Settings(object):
    
    def getStartDelaySeconds(self):
        return 5

    def getTimeFrameMilliseconds(self):
        return 100

    def hasFrontBumper(self):
        return False

    def hasFrontDistanceSensor(self):
        return False

    def getRightDistanceSensorAddress(self):
        return 'in1'

    def getLeftDistanceSensorAddress(self):
        return 'in2'

    def getFrontDistanceSensorAddress(self):
        return None

if __name__ == "__main__":
    logging.info('Loading')
    ev3.Sound.speak('Loading').wait()
    settings = Settings()
    folkracer = Folkracer(Steering(), None, Distances(settings), Buttons(), settings, None, None, LightsAndSounds())
    folkracer.start()
    folkracer.join()
    logging.info('Shutting down.')
    ev3.Sound.speak('Shutting down').wait()
