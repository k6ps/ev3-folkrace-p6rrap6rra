import unittest
from unittest.mock import MagicMock
from tests.ev3dev_test_util import Ev3devTestUtil
Ev3devTestUtil.create_fake_ev3dev_module()
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