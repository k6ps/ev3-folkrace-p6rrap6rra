import unittest
from unittest.mock import MagicMock
ev3dev_mock = MagicMock()
ev3_mock = MagicMock()
import sys
sys.modules["ev3dev"] = ev3dev_mock
sys.modules["ev3dev.ev3"] = ev3_mock
from lights_and_sounds import LightsAndSounds


class LightsAndSoundsUnitTest(unittest.TestCase):

    def setUp(self):
        self.lights_and_sounds = LightsAndSounds()
        self.lights_and_sounds.ev3_sound = MagicMock()

    def test_shouldCallEV3BeepWhenStartDelaySecondCalled(self):
        #given

        #when
        self.lights_and_sounds.startDelaySecond()

        #then
        self.lights_and_sounds.ev3_sound.beep.assert_called_once()