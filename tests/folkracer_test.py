import unittest
from unittest.mock import Mock
from folkracer import *
from steering import Steering

class FolkracerUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.steering = Steering()
        self.steering.initialize = Mock()
        self.folkracer = Folkracer(self.steering)

    def test_shouldInitializeSteeringOnStartup(self):
        #given

        #when

        #then
        self.steering.initialize.assert_called()

    def test_shouldBeOnAwaitingStartStateOnStartup(self):
        #given

        #when

        #then
        self.assertTrue(self.folkracer.getState() is State.AWAITING_START)
        
if __name__ == '__main__':
    unittest.main()