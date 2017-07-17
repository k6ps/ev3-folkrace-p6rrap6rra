import ev3dev.ev3 as ev3

class LightsAndSounds(object):

    def startDelaySecond(self):
        ev3.Sound.beep()