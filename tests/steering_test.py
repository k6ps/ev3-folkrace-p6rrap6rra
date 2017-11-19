import unittest
from unittest.mock import MagicMock
from tests.ev3dev_test_util import Ev3devTestUtil
Ev3devTestUtil.create_fake_ev3dev_module()
from steering import Steering


class SteeringUnitTest(unittest.TestCase):

    def setUp(self):
        self.settings = MagicMock()

    def test_shouldReadSteeringMotorAddressFromSettings(self):
        # given

        # when
        self.steering = Steering(self.settings)

        # then
        self.settings.getSteeringMotorAddress.assert_called_once()
        self.assertIsNotNone(self.steering.steering_motor)

    def test_shouldReadSteeringMotorSpeedFactorFromSettings(self):
        # given

        # when
        self.steering = Steering(self.settings)

        # then
        self.settings.getSteeringMotorSpeedFactor.assert_called_once()

    def test_shouldReadSteeringSpeedFromSettings(self):
        # given

        # when
        self.steering = Steering(self.settings)

        # then
        self.settings.getSteeringSpeed.assert_called_once()

    def test_shouldReadSteeringMaxRangeFromSettings(self):
        # given

        # when
        self.steering = Steering(self.settings)

        # then
        self.settings.getSteeringMaxRange.assert_called_once()

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedLeft(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = -21

        # when
        __actual_steering_position = self.steering.get_current_steering_position()

        # then
        __expected_steering_position = int(-21 * 100 / 47)
        self.assertEqual(__expected_steering_position, __actual_steering_position)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedMaxLeft(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = -47

        # when
        __actual_steering_position = self.steering.get_current_steering_position()

        # then
        self.assertEqual(-100, __actual_steering_position)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedRight(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 18

        # when
        __actual_steering_position = self.steering.get_current_steering_position()

        # then
        __expected_steering_position = int(18 * 100 / 47)
        self.assertEqual(__expected_steering_position, __actual_steering_position)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedMaxRight(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 47

        # when
        __actual_steering_position = self.steering.get_current_steering_position()

        # then
        self.assertEqual(100, __actual_steering_position)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenAtCenter(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 0

        # when
        __actual_steering_position = self.steering.get_current_steering_position()

        # then
        self.assertEqual(0, __actual_steering_position)

    def test_shouldResetSteeringPositionToCenterWhenInitialized(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 32

        # when
        self.steering.initialize()

        # then
        self.assertEqual(0, self.steering.get_current_steering_position())

    def test_shouldTurnMaxRangePlusCompensationRightForCenteringWhenInitialized(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 32

        # when
        self.steering.initialize()

        # then
        self.steering.steering_motor.run_to_rel_pos.assert_called_with(position_sp=-(47 + 7), speed_sp=(10 * 123), stop_action='hold')

    def test_should_turn_steering_motor_left_by_correct_amount_when_steering_motor_position_was_zero(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 0

        # when
        self.steering.set_steering_position(-50)

        # then
        __expected_steering_motor_turn = int(-50 * 47 / 100)
        self.steering.steering_motor.run_to_rel_pos.assert_called_with(position_sp=__expected_steering_motor_turn, speed_sp=(10 * 123), stop_action='hold')

    def test_should_turn_steering_motor_right_by_correct_amount_when_steering_motor_position_was_zero(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 0

        # when
        self.steering.set_steering_position(66)

        # then
        __expected_steering_motor_turn = int(66 * 47 / 100)
        self.steering.steering_motor.run_to_rel_pos.assert_called_with(position_sp=__expected_steering_motor_turn, speed_sp=(10 * 123), stop_action='hold')

    def test_should_turn_steering_motor_left_by_correct_amount_when_steering_motor_position_was_in_left(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = -10

        # when
        self.steering.set_steering_position(-50)

        # then
        __expected_steering_motor_turn = int(-50 * 47 / 100) + 10
        self.steering.steering_motor.run_to_rel_pos.assert_called_with(position_sp=__expected_steering_motor_turn, speed_sp=(10 * 123), stop_action='hold')

    def test_should_turn_steering_motor_left_by_correct_amount_when_steering_motor_position_was_in_right(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 15

        # when
        self.steering.set_steering_position(-50)

        # then
        __expected_steering_motor_turn = int(-50 * 47 / 100) - 15
        self.steering.steering_motor.run_to_rel_pos.assert_called_with(position_sp=__expected_steering_motor_turn, speed_sp=(10 * 123), stop_action='hold')

    def test_should_turn_steering_motor_right_by_correct_amount_when_steering_motor_position_was_in_right(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 15

        # when
        self.steering.set_steering_position(60)

        # then
        __expected_steering_motor_turn = int(60 * 47 / 100) - 15
        self.steering.steering_motor.run_to_rel_pos.assert_called_with(position_sp=__expected_steering_motor_turn, speed_sp=(10 * 123), stop_action='hold')

    def test_should_turn_steering_motor_right_by_correct_amount_when_steering_motor_position_was_in_left(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = -20

        # when
        self.steering.set_steering_position(60)

        # then
        __expected_steering_motor_turn = int(60 * 47 / 100) + 20
        self.steering.steering_motor.run_to_rel_pos.assert_called_with(position_sp=__expected_steering_motor_turn, speed_sp=(10 * 123), stop_action='hold')

