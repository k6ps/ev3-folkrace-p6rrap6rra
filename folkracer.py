from enum import Enum
import ev3dev.ev3 as ev3
from ev3dev.ev3 import Button

class State(Enum):
    AWAITING_START = 0
    STARTING = 1

buttons = ev3.Button()

class Folkracer(object):

    def __init__(self,steering):
        self.steering = steering
        self.steering.initialize()
        self.state = State.AWAITING_START
        while 1:
            if buttons.enter:
                self.state = State.STARTING
                break
            

    def getState(self):
        return self.state

    
