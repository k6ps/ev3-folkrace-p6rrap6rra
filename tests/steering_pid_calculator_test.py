import unittest
import time
from folkracer import SteeringPIDCalculator

FINAL_PID_OUTPUT_ERROR_TOLERANCE = 0.02
CYCLE_LENGTH_SECONDS = 0.01


class SteeringPIDCalculatorUnitTest(unittest.TestCase):

    def setUp(self):
        self.steering_pid_calculator = SteeringPIDCalculator()
        self.steering_pid_calculator.reset()

    def test_shouldGetOutputToNearZeroWhenSetpointMovedToOne(self):
        # given
        number_of_cycles = 25
        feedback = 0.0
        output = 0.0

        # when
        for i in range(1, number_of_cycles):
            output = self.steering_pid_calculator.calculate(feedback)
            feedback += output
            if (i > 9):
                self.steering_pid_calculator.set_set_point(1)
            time.sleep(CYCLE_LENGTH_SECONDS)

        # then
        self.assertAlmostEqual(0.0, output, delta=FINAL_PID_OUTPUT_ERROR_TOLERANCE)

    def test_shouldGetOutputToNearZeroWhenSetpointMovedToMinusOne(self):
        # given
        number_of_cycles = 25
        feedback = 0.0
        output = 0.0

        # when
        for i in range(1, number_of_cycles):
            output = self.steering_pid_calculator.calculate(feedback)
            feedback += output
            if (i > 9):
                self.steering_pid_calculator.set_set_point(-1)
            time.sleep(CYCLE_LENGTH_SECONDS)

        # then
        self.assertAlmostEqual(0.0, output, delta=FINAL_PID_OUTPUT_ERROR_TOLERANCE)

    def test_shouldGetOutputToNearZeroWhenSetpointMovedToHundred(self):
        # given
        number_of_cycles = 50
        feedback = 0.0
        output = 0.0

        # when
        for i in range(1, number_of_cycles):
            output = self.steering_pid_calculator.calculate(feedback)
            feedback += output
            if (i > 9):
                self.steering_pid_calculator.set_set_point(100)
            time.sleep(CYCLE_LENGTH_SECONDS)

        # then
        self.assertAlmostEqual(0.0, output, delta=FINAL_PID_OUTPUT_ERROR_TOLERANCE)

    def test_shouldGetOutputToNearZeroWhenSetpointMovedToMinusHundred(self):
        # given
        number_of_cycles = 50
        feedback = 0.0
        output = 0.0

        # when
        for i in range(1, number_of_cycles):
            output = self.steering_pid_calculator.calculate(feedback)
            feedback += output
            if (i > 9):
                self.steering_pid_calculator.set_set_point(-100)
            time.sleep(CYCLE_LENGTH_SECONDS)

        # then
        self.assertAlmostEqual(0.0, output, delta=FINAL_PID_OUTPUT_ERROR_TOLERANCE)

    def test_shouldGetOutputToNearZeroWhenSetpointJumpsBackAndForth(self):
        # given
        number_of_cycles = 100
        feedback = 0.0
        output = 0.0

        # when
        for i in range(1, number_of_cycles):
            output = self.steering_pid_calculator.calculate(feedback)
            feedback += output
            if (i > 9):
                self.steering_pid_calculator.set_set_point(-10)
            if (i > 39):
                self.steering_pid_calculator.set_set_point(10)
            if (i > 69):
                self.steering_pid_calculator.set_set_point(-25)
            time.sleep(CYCLE_LENGTH_SECONDS)

        # then
        self.assertAlmostEqual(0.0, output, delta=FINAL_PID_OUTPUT_ERROR_TOLERANCE)

    def test_shouldGetOutputToNearZeroWhenSetpointStaysAtZero(self):
        # given
        number_of_cycles = 25
        feedback = 0.0
        output = 0.0

        # when
        for i in range(1, number_of_cycles):
            output = self.steering_pid_calculator.calculate(feedback)
            feedback += output
            if (i > 9):
                self.steering_pid_calculator.set_set_point(0)
            time.sleep(CYCLE_LENGTH_SECONDS)

        # then
        self.assertAlmostEqual(0.0, output, delta=FINAL_PID_OUTPUT_ERROR_TOLERANCE)

    def test_shouldGetOutputToNearZeroWhenSetpointMovesConstantlyBySmallSteps(self):
        # given
        number_of_cycles = 100
        feedback = 0.0
        output = 0.0

        # when
        for i in range(1, number_of_cycles):
            output = self.steering_pid_calculator.calculate(feedback)
            feedback += output
            if (i > 9):
                self.steering_pid_calculator.set_set_point(1)
            if (i > 19):
                self.steering_pid_calculator.set_set_point(2)
            if (i > 29):
                self.steering_pid_calculator.set_set_point(3)
            if (i > 39):
                self.steering_pid_calculator.set_set_point(2)
            if (i > 49):
                self.steering_pid_calculator.set_set_point(1)
            if (i > 59):
                self.steering_pid_calculator.set_set_point(-1)
            if (i > 69):
                self.steering_pid_calculator.set_set_point(0)
            if (i > 79):
                self.steering_pid_calculator.set_set_point(2)
            time.sleep(CYCLE_LENGTH_SECONDS)

        # then
        self.assertAlmostEqual(0.0, output, delta=FINAL_PID_OUTPUT_ERROR_TOLERANCE)
