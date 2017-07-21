import ev3dev.ev3 as ev3

class Buttons(object):

    def __init__(self):
        self.ev3_buttons = ev3.Buttons()

    def addStartButtonListener(self, start_button_listener):
        self.ev3_buttons.on_up = start_button_listener.startButtonPressed
        self.ev3_buttons.on_down = start_button_listener.startButtonPressed
        self.ev3_buttons.on_left = start_button_listener.startButtonPressed
        self.ev3_buttons.on_right = start_button_listener.startButtonPressed
