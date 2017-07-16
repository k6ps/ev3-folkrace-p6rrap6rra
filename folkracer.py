from enum import Enum
#import ev3dev.ev3 as ev3
#from ev3dev.ev3 import Button

class State(Enum):
    AWAITING_START = 0
    STARTING = 1

#buttons = ev3.Button()

class Folkracer(object):

    def __init__(self, steering, engine, distances, buttons, settings, orientation, notifications, log):

        self.steering = steering
        self.steering.initialize()
        self.engine = engine
        self.distances = distances
        self.buttons = buttons
        self.buttons.addStartButtonListener(self)
        self.settings = settings
        self.orientation = orientation
        self.notifications = notifications
        self.log = log
        self.state = State.AWAITING_START
        #while 1:
        #   if buttons.enter:
        #       break

    def getState(self):
        return self.state

    def startButtonPressed(self):
       self.state = State.STARTING

    
