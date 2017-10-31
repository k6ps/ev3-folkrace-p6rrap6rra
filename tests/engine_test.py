import unittest
from unittest.mock import Mock, MagicMock, patch
ev3dev_mock = MagicMock()
ev3_mock = MagicMock()
import sys
sys.modules["ev3dev"] = ev3dev_mock
sys.modules["ev3dev.ev3"] = ev3_mock
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
    