import unittest
import time
from unittest.mock import Mock, MagicMock, patch
#ev3dev_mock = MagicMock()
#ev3_mock = MagicMock()
#import sys
#sys.modules["ev3dev"] = ev3dev_mock
#sys.modules["ev3dev.ev3"] = ev3_mock

from folkracer import *
from steering import Steering

class FolkracerUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.steering = Steering()
        self.steering.initialize = Mock()
        self.engine = MagicMock()
        self.distances = MagicMock()
        self.buttons = MagicMock()
        self.settings = MagicMock()
        self.folkracer = Folkracer(self.steering, self.engine, self.distances, self.buttons, self.settings, MagicMock(), MagicMock(), MagicMock())

    def test_shouldInitializeSteeringOnStartup(self):
        #given

        #when

        #then
        self.steering.initialize.assert_called()

    def test_shouldRegisterStartButtonListenerOnStartup(self):
        #given

        #when

        #then
        self.buttons.addStartButtonListener.assert_called_with(self.folkracer)

    def test_shouldBeOnAwaitingStartStateOnStartup(self):
        #given

        #when

        #then
        self.assertTrue(self.folkracer.getState() is State.AWAITING_START)

    def test_shouldBeOnStartingModeWhenStartButtonPressed(self):
        #given

        #when
        self.folkracer.startButtonPressed()
        
        #then
        self.assertTrue(self.folkracer.getState() is State.STARTING)
        
    @patch('time.sleep', return_value=None)
    def test_shouldDelayPredefinedSecondsWhenStartButtonPressed(self, patched_time_sleep):
        #given
        start_delay_seconds = 3
        self.settings.getStartDelaySeconds.return_value = start_delay_seconds

        #when
        self.folkracer.startButtonPressed()
        
        #then
        self.assertEqual(start_delay_seconds, time.sleep.call_count)
        
if __name__ == '__main__':
    unittest.main()