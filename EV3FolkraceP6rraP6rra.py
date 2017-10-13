#/usr/bin/python3

import ev3dev.ev3 as ev3
import logging
from folkracer import Folkracer
from steering import Steering
from buttons import Buttons
from lights_and_sounds import LightsAndSounds

logging.basicConfig(format='%(asctime)s %(message)s', filename='folkracer.log', level=logging.DEBUG)

class Settings(object):
    
    def getStartDelaySeconds(self):
        return 5

if __name__ == "__main__":
    logging.info('Loading')
    ev3.Sound.speak('Loading').wait()
    folkracer = Folkracer(Steering(), None, None, Buttons(), Settings(), None, None, LightsAndSounds())
    folkracer.run()
    logging.info('Shutting down.')
    ev3.Sound.speak('Shutting down').wait()
