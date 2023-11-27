import unittest
from motorcycle import Motorcycle
from car import Car


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.test_moto = Motorcycle("Honda", "CBR", 2020)
        self.test_car = Car("Toyota", "Corolla", 2020)

    def test_init(self):
        self.assertIsInstance(self.test_moto, Motorcycle)
        self.assertIsInstance(self.test_car, Car)

    def test_wheels(self):
        self.assertEqual(self.test_moto.getNumWheels(), 2)
        self.assertEqual(self.test_car.getNumWheels(), 4)

    def test_speed(self):
        self.test_moto.testDrive()
        self.test_car.testDrive()
        self.assertEqual(self.test_moto.getSpeed(), 75)
        self.assertEqual(self.test_car.getSpeed(), 60)

    def test_stop(self):
        self.test_moto.testDrive()
        self.test_car.testDrive()
        print(self.test_moto.getSpeed())
        print(self.test_car.getSpeed())
        self.test_moto.park()
        self.test_car.park()
        print(self.test_moto.getSpeed())
        print(self.test_car.getSpeed())
        self.assertEqual(self.test_moto.getSpeed(), 0)
        self.assertEqual(self.test_car.getSpeed(), 0)

    def tearDown(self):
        del self.test_car
        del self.test_moto


if __name__ == "__main__":
    unittest.main()
