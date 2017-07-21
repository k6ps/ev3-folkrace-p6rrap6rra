import unittest
from unittest.mock import Mock, MagicMock, patch
ev3dev_mock = MagicMock()
ev3_mock = MagicMock()
import sys
sys.modules["ev3dev"] = ev3dev_mock
sys.modules["ev3dev.ev3"] = ev3_mock
from buttons import Buttons

class ButtonsUnitTest(unittest.TestCase):

    def setUp(self):
        self.buttons = Buttons()
        self.start_button_listener = MagicMock()
        self.ev3_buttons = MagicMock()
        self.buttons.ev3_buttons = self.ev3_buttons

    def test_shouldFireStartButtonPressedWhenEV3UpButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        self.ev3_buttons.on_up()

        #then
        self.start_button_listener.startButtonPressed.assert_called_once()

    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3UpButtonPressed(self):
        #given

        #when 
        self.ev3_buttons.on_up()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    def test_shouldFireStartButtonPressedWhenEV3DownButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        self.ev3_buttons.on_down()

        #then
        self.start_button_listener.startButtonPressed.assert_called_once()

    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3DownButtonPressed(self):
        #given

        #when 
        self.ev3_buttons.on_down()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    def test_shouldFireStartButtonPressedWhenEV3LeftButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        self.ev3_buttons.on_left()

        #then
        self.start_button_listener.startButtonPressed.assert_called_once()

    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3LeftButtonPressed(self):
        #given

        #when 
        self.ev3_buttons.on_left()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    def test_shouldFireStartButtonPressedWhenEV3RightButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        self.ev3_buttons.on_right()

        #then
        self.start_button_listener.startButtonPressed.assert_called_once()

    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3RightButtonPressed(self):
        #given

        #when 
        self.ev3_buttons.on_right()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

if __name__ == '__main__':
    unittest.main()
