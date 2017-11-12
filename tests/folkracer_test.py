import unittest
import time
from unittest.mock import Mock, MagicMock
from folkracer import Folkracer, State
from steering import Steering


class FolkracerUnitTest(unittest.TestCase):

    def _assertCloseEnough(self, expected, actual, allowed_margin):
        min_allowed = expected - allowed_margin
        max_allowed = expected + allowed_margin
        self.assertTrue(actual <= max_allowed)
        self.assertTrue(actual >= min_allowed)
    
    def setUp(self):
        self.settings = MagicMock()
        self.steering = Steering(self.settings)
        self.steering.initialize = Mock()
        self.engine = MagicMock()
        self.distances = MagicMock()
        self.bumpers = MagicMock()
        self.buttons = MagicMock()
        self.time_frame_milliseconds = 100
        self.settings.getTimeFrameMilliseconds.return_value = self.time_frame_milliseconds
        self.lights_and_sounds = MagicMock()
        self.folkracer = Folkracer(self.steering, self.engine, self.distances, self.bumpers, self.buttons, self.settings, MagicMock(), MagicMock(), self.lights_and_sounds)
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

    def test_shouldReadDistancesOnceEveryTimeframeWhenInRunningState(self):
        # given
        test_frame_count = 7

        # when
        self.folkracer.enterRunningState()
        time.sleep(test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self._assertCloseEnough(test_frame_count, self.distances.getDistances.call_count, 1)
        
    def test_shouldNotReadDistancesOnceEveryTimeframeWhenInStartingState(self):
        # given
        test_frame_count = 7

        # when
        self.folkracer.enterStartingState()
        time.sleep(test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.distances.getDistances.assert_not_called()
        
    def test_shouldNotReadDistancesOnceEveryTimeframeWhenInAwaitingStartState(self):
        # given
        test_frame_count = 7

        # when
        self.folkracer.enterAwaitingStartState()
        time.sleep(test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.distances.getDistances.assert_not_called()

    def test_shouldCheckBumpersOnceEveryTimeframeWhenInRunningState(self):
        # given
        test_frame_count = 7

        # when
        self.folkracer.enterRunningState()
        time.sleep(test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self._assertCloseEnough(test_frame_count, self.bumpers.getBumperStatuses.call_count, 1)

    def test_shouldNotCheckBumpersOnceEveryTimeframeWhenInStartingState(self):
        # given
        test_frame_count = 7

        # when
        self.folkracer.enterStartingState()
        time.sleep(test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.bumpers.getBumperStatuses.assert_not_called()


    def test_shouldNotCheckBumpersOnceEveryTimeframeWhenInAwaitingStartState(self):
        # given
        test_frame_count = 7

        # when
        self.folkracer.enterAwaitingStartState()
        time.sleep(test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.bumpers.getBumperStatuses.assert_not_called()

if __name__ == '__main__':
    unittest.main()