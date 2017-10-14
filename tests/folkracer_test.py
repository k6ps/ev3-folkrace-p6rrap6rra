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
        self.settings.getTimeFrameMilliseconds.return_value = 100
        self.lights_and_sounds = MagicMock()
        self.folkracer = Folkracer(self.steering, self.engine, self.distances, self.buttons, self.settings, MagicMock(), MagicMock(), self.lights_and_sounds)
        self.folkracer.start()

    def tearDown(self):
        time.sleep(0.1)
        self.folkracer.stop()

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
        time.sleep(start_delay_seconds + 1)
        
        #then
        self.assertEqual(start_delay_seconds, self.lights_and_sounds.startDelaySecond.call_count)

    def test_shouldBeOnRunningModeWhenPredefinedStartingSecondsArePassed(self):
        # given
        start_delay_seconds = 1
        self.settings.getStartDelaySeconds.return_value = start_delay_seconds
        
        # when
        self.folkracer.startButtonPressed()
        time.sleep(start_delay_seconds + 1)

        # then
        self.assertEqual(State.RUNNING, self.folkracer.getState())

    def test_shouldStartDistanceMeasuringProcessWhenEnteringRunningState(self):
        # given

        # when
        self.folkracer.enterRunningState()

        # then
        self.distances.start.assert_called()

    def test_shouldReadDistancesOnceEveryTimeframeWhenInRunningState(self):
        # given
        time_frame_milliseconds = 100
        self.settings.getTimeFrameMilliseconds.return_value = time_frame_milliseconds
        test_frame_count = 7

        # when
        self.folkracer.enterRunningState()
        time.sleep((test_frame_count * time_frame_milliseconds * 0.001) + 0.05)

        # then
        self.assertEqual(test_frame_count, self.distances.getDistances.call_count)
        

if __name__ == '__main__':
    unittest.main()