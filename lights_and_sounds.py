import ev3dev.ev3 as ev3


class LightsAndSounds(object):

    def __init__(self):
        self.ev3_sound = ev3.Sound()

    def startDelaySecond(self):
        self.ev3_sound.beep()