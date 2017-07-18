import unittest
from unittest.mock import Mock, MagicMock, patch
ev3dev_mock = MagicMock()
ev3_mock = MagicMock()
import sys
sys.modules["ev3dev"] = ev3dev_mock
sys.modules["ev3dev.ev3"] = ev3_mock
from lights_and_sounds import LightsAndSounds

class LightsAndSoundsUnitTest(unittest.TestCase):

    def setUp(self):
        self.lights_and_sounds = LightsAndSounds()

    @patch('ev3dev.ev3.Sound.beep')
    def test_shouldCallEV3BeepWhenStartDelaySecondCalled(self, patched_beep):
        #given

        #when
        self.lights_and_sounds.startDelaySecond()

        #then
        patched_beep.assert_called_once()