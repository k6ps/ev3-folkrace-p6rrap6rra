import unittest
import time
from unittest.mock import Mock, MagicMock, patch
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
        self.lights_and_sounds = MagicMock()
        self.folkracer = Folkracer(self.steering, self.engine, self.distances, self.buttons, self.settings, MagicMock(), MagicMock(), self.lights_and_sounds)

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
        time.sleep(0.1)
        
        #then
        self.assertEqual(State.STARTING, self.folkracer.getState())
        
    def test_shouldRemoveStartButtonListenerAfterStartButtonPressed(self):
        #given

        #when
        self.folkracer.startButtonPressed()
        time.sleep(0.1)
        
        #then
        self.buttons.removeStartButtonListener.assert_called()

    def test_shouldNotifyPredefinedSecondsWhenStartButtonPressed(self):
        #given
        start_delay_seconds = 3
        self.settings.getStartDelaySeconds.return_value = start_delay_seconds

        #when
        self.folkracer.startButtonPressed()
        time.sleep(start_delay_seconds + 0.1)
        
        #then
        self.assertEqual(start_delay_seconds, self.lights_and_sounds.startDelaySecond.call_count)

    def test_shouldBeOnRunningModeWhenPredefinedStartingSecondsArePassed(self):
        # given
        start_delay_seconds = 1
        self.settings.getStartDelaySeconds.return_value = start_delay_seconds
        
        # when
        self.folkracer.startButtonPressed()
        time.sleep(start_delay_seconds + 0.1)

        # then
        self.assertEqual(State.RUNNING, self.folkracer.getState())

    def test_shouldStartDistanceMeasuringProcessWhenEnteringRunningState(self):
        # given
        start_delay_seconds = 1
        self.settings.getStartDelaySeconds.return_value = start_delay_seconds

        # when
        self.folkracer.startButtonPressed()
        time.sleep(start_delay_seconds + 0.1)

        # then
        self.distances.start.assert_called()

if __name__ == '__main__':
    unittest.main()