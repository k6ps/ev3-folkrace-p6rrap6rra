import time
import logging
from enum import Enum
from threading import Thread

class State(Enum):
    AWAITING_START = 0
    STARTING = 1
    RUNNING = 2

class StartDelaySecondsRunner(Thread):

    def __init__(self, folkracer):
        Thread.__init__(self)
        self.folkracer = folkracer

    def run(self):
        start_delay_seconds = self.folkracer.settings.getStartDelaySeconds()
        for _ in range(0, start_delay_seconds):
            time.sleep(1)
            self.folkracer.lights_and_sounds.startDelaySecond()
        self.folkracer.enterRunningState()

class Folkracer(Thread):

    def __init__(self, steering, engine, distances, buttons, settings, orientation, log, lights_and_sounds):
        Thread.__init__(self)
        self.steering = steering
        self.steering.initialize()
        self.engine = engine
        self.distances = distances
        self.buttons = buttons
        self.settings = settings
        self.orientation = orientation
        self.log = log
        self.lights_and_sounds = lights_and_sounds
        self._stop_requested = False
        self.setDaemon(True)
        self.enterAwaitingStartState()

    def enterAwaitingStartState(self):
        logging.debug('Entering AWAITING_START state')
        self.state = State.AWAITING_START
        self.buttons.start()
        self.buttons.addStartButtonListener(self)

    def enterRunningState(self):
        logging.debug('Entering RUNNING state')
        self.state = State.RUNNING
        self.distances.start()

    def enterStartingState(self):
        logging.debug('Entering STARTING state')
        self.state = State.STARTING
        self.buttons.removeStartButtonListener()
        StartDelaySecondsRunner(self).start()

    def run(self):
        logging.debug('Folkracer started')
        time_frame_length_seconds = 0.001 * self.settings.getTimeFrameMilliseconds()
        while (self._stop_requested == False):
            if (State.RUNNING == self.getState()):
                distances = self.distances.getDistances()
                logging.debug('distances = ' + str(distances))
            time.sleep(time_frame_length_seconds)
        logging.debug('Folkracer stopped')

    def getState(self):
        return self.state

    def startButtonPressed(self):
        self.enterStartingState()

    def stop(self):
        self._stop_requested == True

