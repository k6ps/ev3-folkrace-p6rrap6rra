import sys
from unittest.mock import MagicMock


class Ev3devTestUtil(object):

    @staticmethod
    def create_fake_ev3dev_module():
        ev3dev_mock = MagicMock()
        ev3_mock = MagicMock()
        sys.modules["ev3dev"] = ev3dev_mock
        sys.modules["ev3dev.ev3"] = ev3_mock
