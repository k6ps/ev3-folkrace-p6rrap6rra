import unittest
from unittest.mock import Mock, MagicMock, patch
ev3dev_mock = MagicMock()
ev3_mock = MagicMock()
#patch.dict("sys.modules", ev3dev.ev3=ev3Mock).start()
import sys
sys.modules["ev3dev"] = ev3dev_mock
sys.modules["ev3dev.ev3"] = ev3_mock

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

    def test_shouldBeOnStartingModeAfterStartButtonIsPushed(self):
        #given

        #when
        self.folkracer.buttons.on_enter('pahh')
        
        #then
        self.assertTrue(self.folkracer.getState() is State.STARTING)
        
if __name__ == '__main__':
    unittest.main()