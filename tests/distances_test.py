import unittest
from unittest.mock import MagicMock
from tests.ev3dev_test_util import Ev3devTestUtil
Ev3devTestUtil.create_fake_ev3dev_module()
from distances import Distances


class DistancesUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.settings = MagicMock()
        self.settings.hasFrontDistanceSensor.return_value = True
        self.settings.getRightDistanceSensorAddress.return_value = "right"
        self.settings.getLeftDistanceSensorAddress.return_value = "left"
        self.settings.getFrontDistanceSensorAddress.return_value = "front"

    def test_shouldReadDistanceSensorSettingsFromSettings(self):
        # given

        # when
        self.distances = Distances(self.settings)

        # then
        self.settings.getRightDistanceSensorAddress.assert_called_once()
        self.settings.getLeftDistanceSensorAddress.assert_called_once()
        self.assertIsNotNone(self.distances.distance_sensor_right)
        self.assertIsNotNone(self.distances.distance_sensor_left)

    def test_shouldNotHaveFrontDistanceSensorWhenDisabledInSettings(self):
        # given
        self.settings.hasFrontDistanceSensor.return_value = False

        # when
        self.distances = Distances(self.settings)

        # then
        self.assertIsNone(self.distances.distance_sensor_front)
        self.settings.getFrontDistanceSensorAddress.assert_not_called()

    def test_shouldHaveFrontDistanceSensorWhenEnabledInSettings(self):
        # given
        self.settings.hasFrontDistanceSensor.return_value = True

        # when
        self.distances = Distances(self.settings)

        # then
        self.assertIsNotNone(self.distances.distance_sensor_front)
        self.settings.getFrontDistanceSensorAddress.assert_called_once()

    def test_shouldReturnCorrectDistanceValues(self):
        # given
        self.distances = Distances(self.settings)
        self.distances.distance_sensor_right = MagicMock()
        self.distances.distance_sensor_left = MagicMock()
        self.distances.distance_sensor_front = MagicMock()
        self.distances.distance_sensor_right.value.return_value = 111
        self.distances.distance_sensor_left.value.return_value = 222
        self.distances.distance_sensor_front.value.return_value = 333

        # when
        actual_distances = self.distances.getDistances()

        # then
        self.assertEqual(11, actual_distances.get('right'))
        self.assertEqual(22, actual_distances.get('left'))
        self.assertEqual(33, actual_distances.get('front'))

    def test_shouldReturnCorrectDistanceValuesWhenFrontSensorDisabled(self):
        # given
        self.settings.hasFrontDistanceSensor.return_value = False
        self.distances = Distances(self.settings)
        self.distances.distance_sensor_right = MagicMock()
        self.distances.distance_sensor_left = MagicMock()
        self.distances.distance_sensor_right.value.return_value = 111
        self.distances.distance_sensor_left.value.return_value = 222

        # when
        actual_distances = self.distances.getDistances()

        # then
        self.assertEqual(11, actual_distances.get('right'))
        self.assertEqual(22, actual_distances.get('left'))
        self.assertFalse('front' in actual_distances)
    