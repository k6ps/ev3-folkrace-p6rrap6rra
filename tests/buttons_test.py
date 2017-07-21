import unittest
from unittest.mock import Mock, MagicMock, patch
ev3dev_mock = MagicMock()
ev3_mock = MagicMock()
import sys
sys.modules["ev3dev"] = ev3dev_mock
sys.modules["ev3dev.ev3"] = ev3_mock
from buttons import Buttons

class EV3ButtonsMock(unittest.mock.Mock):
    
    def __init__(self):
        self.on_up = None

class ButtonsUnitTest(unittest.TestCase):

    def setUp(self):
        self.buttons = Buttons()
        self.start_button_listener = MagicMock()

    @patch('ev3dev.ev3.Buttons')
    def test_shouldFireStartButtonPressedWhenEV3UpButtonPressed(self, ev3_buttons_mock):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        ev3_buttons_mock.on_up()

        #then
        self.start_button_listener.startButtonPressed.assert_called_once()

    @patch('ev3dev.ev3.Buttons')
    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3UpButtonPressed(self, ev3_buttons_mock):
        #given

        #when 
        ev3_buttons_mock.on_up()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    @patch('ev3dev.ev3.Buttons')
    def test_shouldFireStartButtonPressedWhenEV3DownButtonPressed(self, ev3_buttons_mock):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        ev3_buttons_mock.on_down()

        #then
        self.start_button_listener.startButtonPressed.assert_called_once()

    @patch('ev3dev.ev3.Buttons')
    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3DownButtonPressed(self, ev3_buttons_mock):
        #given

        #when 
        ev3_buttons_mock.on_down()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    @patch('ev3dev.ev3.Buttons')
    def test_shouldFireStartButtonPressedWhenEV3LeftButtonPressed(self, ev3_buttons_mock):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        ev3_buttons_mock.on_left()

        #then
        self.start_button_listener.startButtonPressed.assert_called_once()

    @patch('ev3dev.ev3.Buttons')
    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3LeftButtonPressed(self, ev3_buttons_mock):
        #given

        #when 
        ev3_buttons_mock.on_left()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    @patch('ev3dev.ev3.Buttons')
    def test_shouldFireStartButtonPressedWhenEV3RightButtonPressed(self, ev3_buttons_mock):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        ev3_buttons_mock.on_right()

        #then
        self.start_button_listener.startButtonPressed.assert_called_once()

    @patch('ev3dev.ev3.Buttons')
    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3RightButtonPressed(self, ev3_buttons_mock):
        #given

        #when 
        ev3_buttons_mock.on_right()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()
