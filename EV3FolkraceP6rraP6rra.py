#!/usr/bin/python3

import ev3dev.ev3 as ev3
import logging
import logging.handlers
import queue
from folkracer import Folkracer
from steering import Steering
from buttons import Buttons
from distances import Distances
from bumpers import Bumpers
from engine import Engine
from lights_and_sounds import LightsAndSounds

log_message_queue = queue.Queue(-1)
queue_handler = logging.handlers.QueueHandler(log_message_queue)
file_handler = logging.FileHandler(filename='folkracer.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(threadName)s]: %(message)s'))
log_message_queue_listener = logging.handlers.QueueListener(log_message_queue, file_handler)
logging.basicConfig(level=logging.DEBUG, handlers=[queue_handler])


class Settings(object):
    
    def getStartDelaySeconds(self):
        return 2

    def getTimeFrameMilliseconds(self):
        return 100

    def hasFrontBumper(self):
        return False

    def getFrontBumperAddress(self):
        return 'in4'

    def hasFrontDistanceSensor(self):
        return False

    def getRightDistanceSensorAddress(self):
        return 'in3'

    def getLeftDistanceSensorAddress(self):
        return 'in2'

    def getFrontDistanceSensorAddress(self):
        return None

    def getMotor1Address(self):
        return 'outB'

    def getMotor2Address(self):
        return 'outD'

    def getMotorSpeedFactor(self):
        return -10

    def getSteeringMotorAddress(self):
        return 'outC'

    def getSteeringMotorSpeedFactor(self):
        return 10

    def getSteeringSpeed(self):
        return 10

    def getSteeringMaxRange(self):
        return 37

    def getSteeringMotorPositionFactor(self):
        return -1

    def getMaxSideDistance(self):
        return 150

    def getMinSideDistance(self):
        return 10

    def getNormSideDistance(self):
        return 50

    def getMaxSteeringError(self):
        return 50


if __name__ == "__main__":
    log_message_queue_listener.start()
    logging.info('Loading')
    ev3.Sound.beep().wait()
    ev3.Sound.beep().wait()
    settings = Settings()
    bumpers = Bumpers(settings.getFrontBumperAddress()) if (settings.hasFrontBumper()) else None
    steering = Steering(
        settings.getSteeringMotorAddress(),
        settings.getSteeringMotorSpeedFactor(),
        settings.getSteeringSpeed(),
        settings.getSteeringMaxRange(),
        settings.getSteeringMotorPositionFactor()
    )
    folkracer = Folkracer(steering, Engine(settings), Distances(settings), bumpers, Buttons(), settings, None, None, LightsAndSounds())
    folkracer.start()
    folkracer.join()
    logging.info('Shutting down.')
    log_message_queue_listener.stop()
    ev3.Sound.beep().wait()
    ev3.Sound.beep().wait()
