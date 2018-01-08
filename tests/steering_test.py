import unittest
from unittest.mock import MagicMock
from tests.ev3dev_test_util import Ev3devTestUtil
Ev3devTestUtil.create_fake_ev3dev_module()
from steering import Steering

TEST_STEERING_MAX_RANGE = 47
TEST_STEERING_SPEED = 10
TEST_STEERING_MOTOR_ADDRESS = 'steering_motor'
TEST_STEERING_MOTOR_POSITION_FACTOR = -1
TEST_STEERING_MOTOR_SPEED_FACTOR = 123
EXPECTED_STEERING_MOTOR_SPEED = TEST_STEERING_MOTOR_SPEED_FACTOR * TEST_STEERING_SPEED
EXPECTED_STEERING_MOTOR_STOP_ACTION = 'coast'


class SteeringUnitTest(unittest.TestCase):

    def setUp(self):
        self.steering = Steering(
            TEST_STEERING_MOTOR_ADDRESS,
            TEST_STEERING_MOTOR_SPEED_FACTOR,
            TEST_STEERING_SPEED,
            TEST_STEERING_MAX_RANGE,
            TEST_STEERING_MOTOR_POSITION_FACTOR,
            True
        )
        self.steering.steering_motor = MagicMock()

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedLeft(self):
        # given
        __test_steering_motor_position = -21
        self.steering.steering_motor.position = __test_steering_motor_position

        # when
        __actual_steering_position = self.steering.get_current_steering_position()

        # then
        __expected_steering_position = self.__get_expected_steering_position(__test_steering_motor_position)
        self.assertEqual(__expected_steering_position, __actual_steering_position)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedMaxLeft(self):
        # given
        self.steering.steering_motor.position = -TEST_STEERING_MAX_RANGE

        # when
        __actual_steering_position = self.steering.get_current_steering_position()

        # then
        __expected_steering_position = TEST_STEERING_MOTOR_POSITION_FACTOR * -100
        self.assertEqual(__expected_steering_position, __actual_steering_position)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedRight(self):
        # given
        __test_steering_motor_position = 18
        self.steering.steering_motor.position = __test_steering_motor_position

        # when
        __actual_steering_position = self.steering.get_current_steering_position()

        # then
        __expected_steering_position = self.__get_expected_steering_position(__test_steering_motor_position)
        self.assertEqual(__expected_steering_position, __actual_steering_position)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedMaxRight(self):
        # given
        self.steering.steering_motor.position = TEST_STEERING_MAX_RANGE

        # when
        __actual_steering_position = self.steering.get_current_steering_position()

        # then
        __expected_steering_position = TEST_STEERING_MOTOR_POSITION_FACTOR * 100
        self.assertEqual(__expected_steering_position, __actual_steering_position)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenAtCenter(self):
        # given
        self.steering.steering_motor.position = 0

        # when
        __actual_steering_position = self.steering.get_current_steering_position()

        # then
        self.assertEqual(0, __actual_steering_position)

    def test_shouldResetSteeringPositionToCenterWhenInitialized(self):
        # given
        self.steering.steering_motor.position = 32

        # when
        self.steering.initialize()

        # then
        self.steering.steering_motor.reset.assert_called_once()

    def test_shouldTurnMaxRangeRightForCenteringWhenInitialized(self):
        # given
        self.steering.steering_motor.position = 32

        # when
        self.steering.initialize()

        # then
        __expected_steering_motor_turn = TEST_STEERING_MOTOR_POSITION_FACTOR * TEST_STEERING_MAX_RANGE
        self.steering.steering_motor.run_to_rel_pos.assert_called_with(
            position_sp=__expected_steering_motor_turn,
            speed_sp=EXPECTED_STEERING_MOTOR_SPEED,
            stop_action=EXPECTED_STEERING_MOTOR_STOP_ACTION
        )

    def test_should_turn_steering_motor_left_by_correct_amount_when_steering_motor_position_was_zero(self):
        # given
        __test_steering_motor_initial_position = 0
        __test_steering_position = -50
        self.steering.steering_motor.position = __test_steering_motor_initial_position

        # when
        self.steering.set_steering_position(__test_steering_position)

        # then
        __expected_steering_motor_turn = self.__get_expected_steering_motor_turn(__test_steering_position)
        self.steering.steering_motor.run_to_abs_pos.assert_called_with(
            position_sp=__expected_steering_motor_turn,
            speed_sp=EXPECTED_STEERING_MOTOR_SPEED,
            stop_action=EXPECTED_STEERING_MOTOR_STOP_ACTION
        )

    def test_should_turn_steering_motor_right_by_correct_amount_when_steering_motor_position_was_zero(self):
        # given
        __test_steering_motor_initial_position = 0
        __test_steering_position = 66
        self.steering.steering_motor.position = __test_steering_motor_initial_position

        # when
        self.steering.set_steering_position(__test_steering_position)

        # then
        __expected_steering_motor_turn = self.__get_expected_steering_motor_turn(__test_steering_position)
        self.steering.steering_motor.run_to_abs_pos.assert_called_with(
            position_sp=__expected_steering_motor_turn,
            speed_sp=EXPECTED_STEERING_MOTOR_SPEED,
            stop_action=EXPECTED_STEERING_MOTOR_STOP_ACTION
        )

    def test_should_turn_steering_motor_left_by_correct_amount_when_steering_motor_position_was_in_left(self):
        # given
        __test_steering_motor_initial_position = -10
        __test_steering_position = -50
        self.steering.steering_motor.position = __test_steering_motor_initial_position

        # when
        self.steering.set_steering_position(__test_steering_position)

        # then
        __expected_steering_motor_turn = self.__get_expected_steering_motor_turn(__test_steering_position)
        self.steering.steering_motor.run_to_abs_pos.assert_called_with(
            position_sp=__expected_steering_motor_turn,
            speed_sp=EXPECTED_STEERING_MOTOR_SPEED,
            stop_action=EXPECTED_STEERING_MOTOR_STOP_ACTION
        )

    def test_should_turn_steering_motor_left_by_correct_amount_when_steering_motor_position_was_in_right(self):
        # given
        __test_steering_motor_initial_position = 15
        __test_steering_position = -50
        self.steering.steering_motor.position = __test_steering_motor_initial_position

        # when
        self.steering.set_steering_position(__test_steering_position)

        # then
        __expected_steering_motor_turn = self.__get_expected_steering_motor_turn(__test_steering_position)
        self.steering.steering_motor.run_to_abs_pos.assert_called_with(
            position_sp=__expected_steering_motor_turn,
            speed_sp=EXPECTED_STEERING_MOTOR_SPEED,
            stop_action=EXPECTED_STEERING_MOTOR_STOP_ACTION
        )

    def test_should_turn_steering_motor_right_by_correct_amount_when_steering_motor_position_was_in_right(self):
        # given
        __test_steering_motor_initial_position = 15
        __test_steering_position = 60
        self.steering.steering_motor.position = __test_steering_motor_initial_position

        # when
        self.steering.set_steering_position(__test_steering_position)

        # then
        __expected_steering_motor_turn = self.__get_expected_steering_motor_turn(__test_steering_position)
        self.steering.steering_motor.run_to_abs_pos.assert_called_with(
            position_sp=__expected_steering_motor_turn,
            speed_sp=EXPECTED_STEERING_MOTOR_SPEED,
            stop_action=EXPECTED_STEERING_MOTOR_STOP_ACTION
        )

    def test_should_turn_steering_motor_right_by_correct_amount_when_steering_motor_position_was_in_left(self):
        # given
        __test_steering_motor_initial_position = -20
        __test_steering_position = 60
        self.steering.steering_motor.position = __test_steering_motor_initial_position

        # when
        self.steering.set_steering_position(__test_steering_position)

        # then
        __expected_steering_motor_turn = self.__get_expected_steering_motor_turn(__test_steering_position)
        self.steering.steering_motor.run_to_abs_pos.assert_called_with(
            position_sp=__expected_steering_motor_turn,
            speed_sp=EXPECTED_STEERING_MOTOR_SPEED,
            stop_action=EXPECTED_STEERING_MOTOR_STOP_ACTION
        )

    @staticmethod
    def __get_expected_steering_motor_turn(desired_steering_position):
        return TEST_STEERING_MOTOR_POSITION_FACTOR * (
            int(desired_steering_position * TEST_STEERING_MAX_RANGE / 100)
        )

    @staticmethod
    def __get_expected_steering_position(steering_motor_position):
        return TEST_STEERING_MOTOR_POSITION_FACTOR * int(steering_motor_position * 100 / TEST_STEERING_MAX_RANGE)
