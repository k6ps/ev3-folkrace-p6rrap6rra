import unittest
from folkracer import Folkracer

class FolkracerUnitTest(unittest.TestCase):
    def test_shouldInitializeSteeringOnStartup(self):
        folkracer = Folkracer()
        self.assertEqual(folkracer.test(), 'Foo!')

if __name__ == '__main__':
    unittest.main()