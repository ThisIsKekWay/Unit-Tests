import unittest

from main import number_interval


class TestNumberInterval(unittest.TestCase):
    def test_number_interval(self):
        self.assertTrue(number_interval(29))
        self.assertFalse(number_interval(0))
        self.assertRaises(TypeError, number_interval, 'foo')
