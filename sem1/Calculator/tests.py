import unittest
from sem1.Calculator import calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.test_subject = calc.Calculator()

    def test_calculation(self):
        self.assertEqual(2, self.test_subject.calculation(1, 1, "+"))
        self.assertEqual(0, self.test_subject.calculation(1, 1, "-"))
        self.assertEqual(1, self.test_subject.calculation(1, 1, "*"))
        self.assertEqual(1, self.test_subject.calculation(1, 1, "/"))
        self.assertRaises(ValueError, self.test_subject.calculation, 1, 1, "!")
        self.assertRaises(ZeroDivisionError, self.test_subject.calculation, 1, 0, "/")
        self.assertRaises(TypeError, self.test_subject.calculation, 1, 'foo', '-')
        self.assertRaises(TypeError, self.test_subject.calculation, 'foo', 1, '-')

    def test_root(self):
        self.assertEqual(2, self.test_subject.squareRoot(4))
        self.assertRaises(ValueError, self.test_subject.squareRoot, -1)
        self.assertRaises(TypeError, self.test_subject.squareRoot, 'foo')

    def test_discount(self):
        self.assertEqual(100, self.test_subject.calculating_discount(100, 0))
        self.assertEqual(50, self.test_subject.calculating_discount(100, 50))
        self.assertRaises(ValueError, self.test_subject.calculating_discount, 100, 101)
        self.assertRaises(ValueError, self.test_subject.calculating_discount, -1, 50)
        self.assertRaises(ValueError, self.test_subject.calculating_discount, 100, -1)
        self.assertRaises(TypeError, self.test_subject.calculating_discount, 100, 'foo')
        self.assertRaises(TypeError, self.test_subject.calculating_discount, 'foo', 50)


if __name__ == '__main__':
    unittest.main()
