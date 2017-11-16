import unittest
from folkracer import SteeringErrorCalculator

class SteeringErrorCalculatorUnitTest(unittest.TestCase):

    def setUp(self):
        self.max_side_distance = 100
        self.norm_side_distance = 60
        self.min_side_distance = 25
        self.max_steering_error_distance = 150
        self.actual_position_calculator = SteeringErrorCalculator(
            self.max_side_distance,
            self.norm_side_distance,
            self.min_side_distance,
            self.max_steering_error_distance
        )

    def test_shouldReturnZeroWhenBothDistancesAreEqual(self):
        # given

        # when
        actual_position = self.actual_position_calculator.calculateSteeringError(65, 65)

        # then
        self.assertEqual(0, actual_position)

    def test_shouldReturnProportionalDifferenceBetweenActualLeftDistanceAndNormalWhenRightDistanceIsAboveMax(self):
        # given

        # when
        actual_position = self.actual_position_calculator.calculateSteeringError(70, 500)

        # then
        expected_steering_error = int((70 - self.norm_side_distance) * 100 / self.max_steering_error_distance)
        self.assertEqual(expected_steering_error, actual_position)

    def test_shouldReturnProportionalDifferenceBetweenActualRightDistanceAndNormalWhenLeftDistanceIsAboveMax(self):
        # given

        # when
        actual_position = self.actual_position_calculator.calculateSteeringError(400, 80)

        # then
        expected_steering_error = int((self.norm_side_distance - 80) * 100 / self.max_steering_error_distance)
        self.assertEqual(expected_steering_error, actual_position)

    def test_shouldReturnZeroWhenBothDistancesAreAboveMax(self):
        # given

        # when
        actual_position = self.actual_position_calculator.calculateSteeringError(550, 660)

        # then
        self.assertEqual(0, actual_position)

    def test_shouldReturnNegativeMaxSteeringErrorWhenRightDistanceIsBelowMinimumSideDistanceAndLeftDistanceIsAboveMinimum(self):
        # given

        # when
        actual_position = self.actual_position_calculator.calculateSteeringError(60, 10)

        # then
        self.assertEqual(-100, actual_position)

    def test_shouldReturnPositiveMaxSteeringErrorWhenLeftDistanceIsBelowMinimumSideDistanceAndRightDistanceIsAboveMinimum(self):
        # given

        # when
        actual_position = self.actual_position_calculator.calculateSteeringError(15, 75)

        # then
        self.assertEqual(100, actual_position)

    def test_shouldReturnDifferenceBetweenRightAndLeftDistancesAsProportionOfMaxSteeringErrorWhenLeftIsBiggerThanRight(self):
        # given

        # when
        actual_position = self.actual_position_calculator.calculateSteeringError(85, 45)

        # then
        expected_steering_error = int((45 - 85) * 100 / self.max_steering_error_distance)
        self.assertEqual(expected_steering_error, actual_position)

    def test_shouldReturnDifferenceBetweenRightAndLeftDistancesAsProportionOfMaxSteeringErrorWhenRightIsBiggerThanLeft(self):
        # given

        # when
        actual_position = self.actual_position_calculator.calculateSteeringError(50, 75)

        # then
        expected_steering_error = int((75 - 50) * 100 / self.max_steering_error_distance)
        self.assertEqual(expected_steering_error, actual_position)
