import time
import ev3dev.ev3 as ev3
from threading import Thread

class Buttons(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.stop_command_received = False
        self.ev3_buttons = ev3.Button()
        self.start_button_listener = None

    def _anyArrowButtonPressed(self):
        return (self.ev3_buttons.up | self.ev3_buttons.down | self.ev3_buttons.left | self.ev3_buttons.right)

    def _hasStartButtonListener(self):
        return (self.start_button_listener != None)
        
    def addStartButtonListener(self, start_button_listener):
        self.start_button_listener = start_button_listener

    def removeStartButtonListener(self):
        self.start_button_listener = None

    def run(self):
        while (self.stop_command_received == False):
            if (self._hasStartButtonListener() & self._anyArrowButtonPressed()):
                self.start_button_listener.startButtonPressed()

    def stop(self):
        self.stop_command_received = True

