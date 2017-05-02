import unittest
from unittest.mock import Mock
from folkracer import *
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

    def test_shouldBeOnAwaitingStartStateWhenInitialized(self):
        #given
        steering = Steering()
        steering.initialize = Mock()

        #when
        folkracer = Folkracer(steering)

        #then
        self.assertTrue(folkracer.getState() is State.AWAITING_START)
        
if __name__ == '__main__':
    unittest.main()