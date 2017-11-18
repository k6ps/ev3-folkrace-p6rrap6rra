import unittest
from unittest.mock import MagicMock
from tests.ev3dev_test_util import Ev3devTestUtil
Ev3devTestUtil.create_fake_ev3dev_module()
from engine import Engine


class EngineUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.settings = MagicMock()

    def test_shouldReadMotorSettingsFromSettings(self):
        # given

        # when
        self.engine = Engine(self.settings)

        # then
        self.settings.getMotor1Address.assert_called_once()
        self.settings.getMotor2Address.assert_called_once()
        self.assertIsNotNone(self.engine.motor_1)
        self.assertIsNotNone(self.engine.motor_2)
    
    def test_shouldReadMotorSpeedFactorFromSettings(self):
        # given

        # when
        self.engine = Engine(self.settings)

        # then
        self.settings.getMotorSpeedFactor.assert_called_once()

    def test_shouldMotorsSpeedUsingSpeedFactor(self):
        # given
        self.settings.getMotor1Address.return_value = 'a_motor'
        self.settings.getMotor2Address.return_value = 'another_motor'
        self.settings.getMotorSpeedFactor.return_value = 123
        self.engine = Engine(self.settings)
        self.engine.motor_1 = MagicMock()
        self.engine.motor_2 = MagicMock()

        # when
        self.engine.setSpeed(65)

        # then
        _expected_speed = 65 * 123
        self.engine.motor_1.run_forever.assert_called_once_with(speed_sp = _expected_speed)
        self.engine.motor_2.run_forever.assert_called_once_with(speed_sp = _expected_speed)
