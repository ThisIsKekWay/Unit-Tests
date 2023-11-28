import unittest
from main import even_odd


class TestEvenOdd(unittest.TestCase):
    def test_even_odd(self):
        self.assertEqual(even_odd(2), True)
        self.assertEqual(even_odd(3), False)


if __name__ == '__main__':
    unittest.main()


