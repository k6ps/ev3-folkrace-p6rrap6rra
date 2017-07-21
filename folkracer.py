import time
from enum import Enum

class State(Enum):
    AWAITING_START = 0
    STARTING = 1

class Folkracer(object):

    def __init__(self, steering, engine, distances, buttons, settings, orientation, log, lights_and_sounds):
        self.steering = steering
        self.steering.initialize()
        self.engine = engine
        self.distances = distances
        self.buttons = buttons
        self.buttons.addStartButtonListener(self)
        self.settings = settings
        self.orientation = orientation
        self.log = log
        self.lights_and_sounds = lights_and_sounds
        self.state = State.AWAITING_START

    def getState(self):
        return self.state

    def startButtonPressed(self):
       self.state = State.STARTING
       start_delay_seconds = self.settings.getStartDelaySeconds()
       for _ in range(0, start_delay_seconds):
           time.sleep(1)
           self.lights_and_sounds.startDelaySecond()
