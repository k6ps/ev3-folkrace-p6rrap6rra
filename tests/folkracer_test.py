import unittest
from unittest.mock import Mock
from folkracer import Folkracer
from steering import Steering

class FolkracerUnitTest(unittest.TestCase):
    def test_shouldInitializeSteeringOnStartup(self):
        #given
        steering = Steering()
        steering.initialize = Mock()

        #when
        folkracer = Folkracer(steering)

        #then
        steering.initialize.assert_called()
if __name__ == '__main__':
    unittest.main()