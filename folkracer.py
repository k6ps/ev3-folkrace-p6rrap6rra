import time
import logging
from enum import Enum
from threading import Thread

class State(Enum):
    AWAITING_START = 0
    STARTING = 1
    RUNNING = 2

class StartingSequenceRunner(Thread):

    def __init__(self, folkracer):
        Thread.__init__(self)
        self.folkracer = folkracer

    def run(self):
        logging.debug('Entering STARTING state')
        self.folkracer.state = State.STARTING
        start_delay_seconds = self.folkracer.settings.getStartDelaySeconds()
        for _ in range(0, start_delay_seconds):
            time.sleep(1)
            self.folkracer.lights_and_sounds.startDelaySecond()
        self.folkracer.state = State.RUNNING
            
class Folkracer(Thread):

    def __init__(self, steering, engine, distances, buttons, settings, orientation, log, lights_and_sounds):
        Thread.__init__(self)
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
        self.setDaemon(True)
        self.state = State.AWAITING_START

    def run(self):
        self.buttons.setDaemon(False)
        self.buttons.start()
        while (True):
            pass

    def getState(self):
        return self.state

    def startButtonPressed(self):
        StartingSequenceRunner(self).start()
        self.buttons.removeStartButtonListener()

