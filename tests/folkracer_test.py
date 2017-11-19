import unittest
import time
from unittest.mock import MagicMock
from folkracer import Folkracer, State

FRAME_COUNT_TEST_ERROR_TOLERANCE = 2
TEST_TIME_FRAME_MILLISECONDS = 100


class FolkracerUnitTest(unittest.TestCase):

    def setUp(self):
        self.settings = MagicMock()
        self.steering = MagicMock()
        self.engine = MagicMock()
        self.distances = MagicMock()
        self.distances.getDistances.return_value = {
            'right':55,
            'left':55
        }
        self.bumpers = MagicMock()
        self.buttons = MagicMock()
        self.time_frame_milliseconds = TEST_TIME_FRAME_MILLISECONDS
        self.settings.getTimeFrameMilliseconds.return_value = self.time_frame_milliseconds
        self.lights_and_sounds = MagicMock()
        self.folkracer = Folkracer(self.steering, self.engine, self.distances, self.bumpers, self.buttons, self.settings, MagicMock(), MagicMock(), self.lights_and_sounds)
        self.folkracer.expected_steering_calculator = MagicMock()
        self.folkracer.expected_steering_calculator.calculate_expected_steering.return_value = 0
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
        __start_delay_seconds = 3
        self.settings.getStartDelaySeconds.return_value = __start_delay_seconds

        #when
        self.folkracer.startButtonPressed()
        time.sleep(__start_delay_seconds + 1)
        
        #then
        self.assertEqual(__start_delay_seconds, self.lights_and_sounds.startDelaySecond.call_count)

    def test_shouldBeOnRunningModeWhenPredefinedStartingSecondsArePassed(self):
        # given
        __start_delay_seconds = 1
        self.settings.getStartDelaySeconds.return_value = __start_delay_seconds
        
        # when
        self.folkracer.startButtonPressed()
        time.sleep(__start_delay_seconds + 1)

        # then
        self.assertEqual(State.RUNNING, self.folkracer.getState())

    def test_shouldReadDistancesOnceEveryTimeframeWhenInRunningState(self):
        # given
        __test_frame_count = 7

        # when
        self.folkracer.enterRunningState()
        time.sleep(__test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.assertAlmostEqual(
            __test_frame_count,
            self.distances.getDistances.call_count,
            delta=FRAME_COUNT_TEST_ERROR_TOLERANCE
        )

    def test_shouldNotReadDistancesOnceEveryTimeframeWhenInStartingState(self):
        # given
        __test_frame_count = 7

        # when
        self.folkracer.enterStartingState()
        time.sleep(__test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.distances.getDistances.assert_not_called()
        
    def test_shouldNotReadDistancesOnceEveryTimeframeWhenInAwaitingStartState(self):
        # given
        __test_frame_count = 7

        # when
        self.folkracer.enterAwaitingStartState()
        time.sleep(__test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.distances.getDistances.assert_not_called()

    def test_shouldCheckBumpersOnceEveryTimeframeWhenInRunningState(self):
        # given
        __test_frame_count = 7

        # when
        self.folkracer.enterRunningState()
        time.sleep(__test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.assertAlmostEqual(
            __test_frame_count,
            self.bumpers.getBumperStatuses.call_count,
            delta=FRAME_COUNT_TEST_ERROR_TOLERANCE
        )

    def test_shouldNotCheckBumpersOnceEveryTimeframeWhenInStartingState(self):
        # given
        __test_frame_count = 7

        # when
        self.folkracer.enterStartingState()
        time.sleep(__test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.bumpers.getBumperStatuses.assert_not_called()

    def test_shouldNotCheckBumpersOnceEveryTimeframeWhenInAwaitingStartState(self):
        # given
        __test_frame_count = 7

        # when
        self.folkracer.enterAwaitingStartState()
        time.sleep(__test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.bumpers.getBumperStatuses.assert_not_called()

    def test_shouldCalculateExpectedSteeringOnceEveryTimeframeWhenInRunningState(self):
        # given
        __test_frame_count = 7

        # when
        self.folkracer.enterRunningState()
        time.sleep(__test_frame_count * self.time_frame_milliseconds * 0.001)

        # then
        self.assertAlmostEqual(
            __test_frame_count,
            self.folkracer.expected_steering_calculator.calculate_expected_steering.call_count,
            delta=FRAME_COUNT_TEST_ERROR_TOLERANCE
        )

if __name__ == '__main__':
    unittest.main()