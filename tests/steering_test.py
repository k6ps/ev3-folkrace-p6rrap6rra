import unittest
from unittest.mock import Mock, MagicMock, patch
ev3dev_mock = MagicMock()
ev3_mock = MagicMock()
import sys
sys.modules["ev3dev"] = ev3dev_mock
sys.modules["ev3dev.ev3"] = ev3_mock
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

