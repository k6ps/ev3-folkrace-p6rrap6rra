from enum import Enum

class State(Enum):
    AWAITING_START = 0
    STARTING = 1

class Folkracer(object):
    def __init__(self,steering):
        self.steering = steering
        self.steering.initialize()
        self.state = State.AWAITING_START

    def getState(self):
        return self.state
