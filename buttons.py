import ev3dev.ev3 as ev3

class Buttons(object):

    def __init__(self):
        self.start_button_listener = None

    def addStartButtonListener(self, start_button_listener):
        self.start_button_listener = start_button_listener
        ev3.Buttons.on_up = self.start_button_listener.startButtonPressed
        ev3.Buttons.on_down = self.start_button_listener.startButtonPressed
        ev3.Buttons.on_left = self.start_button_listener.startButtonPressed
        ev3.Buttons.on_right = self.start_button_listener.startButtonPressed
