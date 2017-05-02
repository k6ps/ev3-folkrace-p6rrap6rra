#/usr/bin/python3

import ev3dev.ev3 as ev3

if __name__ == "__main__":
    ev3.Sound.speak('Welcome to the E V 3 dev project!').wait()