import ev3dev.ev3 as ev3


class Bumpers():

    def __init__(self, front_bumper_address):
        self.front_bumper = ev3.TouchSensor(address=front_bumper_address)

    def getBumperStatuses(self):
        return self.front_bumper.is_pressed
