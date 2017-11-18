import unittest
from folkracer import ExpectedSteeringCalculator

TEST_MAX_STEERING_ERROR_DISTANCE = 150
TEST_MIN_SIDE_DISTANCE = 25
TEST_NORM_SIDE_DISTANCE = 60
TEST_MAX_SIDE_DISTANCE = 100

class ExpectedSteeringCalculatorUnitTest(unittest.TestCase):

    def setUp(self):
        self.max_side_distance = TEST_MAX_SIDE_DISTANCE
        self.norm_side_distance = TEST_NORM_SIDE_DISTANCE
        self.min_side_distance = TEST_MIN_SIDE_DISTANCE
        self.max_steering_error_distance = TEST_MAX_STEERING_ERROR_DISTANCE
        self.expected_steering_calculator = ExpectedSteeringCalculator(
            self.max_side_distance,
            self.norm_side_distance,
            self.min_side_distance,
            self.max_steering_error_distance
        )

    def __getAbsoluteDistanceDifferenceAsProportionOfMaxSteeringErrorDistance(self, first_distance, second_distance):
        return int(abs(first_distance - second_distance) * 100 / self.max_steering_error_distance)

    def test_shouldReturnZeroWhenBothDistancesAreEqual(self):
        # given

        # when
        actual_expected_steering = self.expected_steering_calculator.calculateExpectedSteering(65, 65)

        # then
        self.assertEqual(0, actual_expected_steering)

    def test_shouldReturnNegativeProportionalDifferenceBetweenActualLeftDistanceAndNormalSideDistanceWhenRightDistanceIsAboveMaxAndLeftDistanceIsAboveNormal(self):
        # given
        distance_left = 70

        # when
        actual_expected_steering = self.expected_steering_calculator.calculateExpectedSteering(distance_left, 500)

        # then
        expected_expected_steering = - self.__getAbsoluteDistanceDifferenceAsProportionOfMaxSteeringErrorDistance(distance_left, self.norm_side_distance)
        self.assertEqual(expected_expected_steering, actual_expected_steering)

    def test_shouldReturnPositiveProportionalDifferenceBetweenActualLeftDistanceAndNormalSideDistanceWhenRightDistanceIsAboveMaxAndLeftDistanceIsBelowNormal(self):
        # given
        distance_left = 45

        # when
        actual_expected_steering = self.expected_steering_calculator.calculateExpectedSteering(distance_left, 500)

        # then
        expected_expected_steering = self.__getAbsoluteDistanceDifferenceAsProportionOfMaxSteeringErrorDistance(distance_left, self.norm_side_distance)
        self.assertEqual(expected_expected_steering, actual_expected_steering)

    def test_shouldReturnNegativeProportionalDifferenceBetweenActualRightDistanceAndNormalSideDistanceWhenLeftDistanceIsAboveMaxAndRightDistanceIsBelowNormal(self):
        # given
        distance_right = 44

        # when
        actual_expected_steering = self.expected_steering_calculator.calculateExpectedSteering(400, distance_right)

        # then
        expected_expected_steering = - self.__getAbsoluteDistanceDifferenceAsProportionOfMaxSteeringErrorDistance(distance_right, self.norm_side_distance)
        self.assertEqual(expected_expected_steering, actual_expected_steering)

    def test_shouldReturnPositiveProportionalDifferenceBetweenActualRightDistanceAndNormalSideDistanceWhenLeftDistanceIsAboveMaxAndRightDistanceIsAboveNormal(self):
        # given
        distance_right = 88

        # when
        actual_expected_steering = self.expected_steering_calculator.calculateExpectedSteering(400, distance_right)

        # then
        expected_expected_steering = self.__getAbsoluteDistanceDifferenceAsProportionOfMaxSteeringErrorDistance(distance_right, self.norm_side_distance)
        self.assertEqual(expected_expected_steering, actual_expected_steering)

    def test_shouldReturnZeroWhenBothDistancesAreAboveMax(self):
        # given

        # when
        actual_expected_steering = self.expected_steering_calculator.calculateExpectedSteering(550, 660)

        # then
        self.assertEqual(0, actual_expected_steering)

    def test_shouldReturnNegativeMaxSteeringErrorWhenRightDistanceIsBelowMinimumSideDistanceAndLeftDistanceIsAboveMinimum(self):
        # given

        # when
        actual_expected_steering = self.expected_steering_calculator.calculateExpectedSteering(60, 10)

        # then
        self.assertEqual(-100, actual_expected_steering)

    def test_shouldReturnPositiveMaxSteeringErrorWhenLeftDistanceIsBelowMinimumSideDistanceAndRightDistanceIsAboveMinimum(self):
        # given

        # when
        actual_expected_steering = self.expected_steering_calculator.calculateExpectedSteering(15, 75)

        # then
        self.assertEqual(100, actual_expected_steering)

    def test_shouldReturnNegativeDifferenceBetweenRightAndLeftDistancesAsProportionOfMaxSteeringErrorWhenLeftIsBiggerThanRight(self):
        # given
        distance_left = 85
        distance_right = 45

        # when
        actual_expected_steering = self.expected_steering_calculator.calculateExpectedSteering(distance_left, distance_right)

        # then
        expected_expected_steering = - self.__getAbsoluteDistanceDifferenceAsProportionOfMaxSteeringErrorDistance(distance_right, distance_left)
        self.assertEqual(expected_expected_steering, actual_expected_steering)

    def test_shouldReturnPositiveDifferenceBetweenRightAndLeftDistancesAsProportionOfMaxSteeringErrorWhenRightIsBiggerThanLeft(self):
        # given
        distance_left = 50
        distance_right = 75

        # when
        actual_expected_steering = self.expected_steering_calculator.calculateExpectedSteering(distance_left, distance_right)

        # then
        expected_expected_steering = self.__getAbsoluteDistanceDifferenceAsProportionOfMaxSteeringErrorDistance(distance_right, distance_left)
        self.assertEqual(expected_expected_steering, actual_expected_steering)
