import unittest

from sem1.Shop.product import Product
from shop import Shop


class ShopTest(unittest.TestCase):
    def test_init(self):
        self.assertRaises(ValueError, Shop, None)
        self.assertRaises(ValueError, Shop, [])
        self.assertRaises(ValueError, Shop, [Product("a", -1)])
        self.assertRaises(ValueError, Shop, [Product("a", 0)])
        self.assertRaises(ValueError, Shop, 'lalalal')
        self.assertRaises(ValueError, Shop, [Product(1, 25)])

    def test_set_products(self):
        self.shop = Shop([Product("b", 25), Product("a", 25)])
        self.assertRaises(ValueError, self.shop.set_products, None)
        self.assertRaises(ValueError, self.shop.set_products, [])
        self.assertRaises(ValueError, self.shop.set_products, [Product("a", -1)])
        self.assertRaises(ValueError, self.shop.set_products, [Product("a", 0)])
        self.assertRaises(ValueError, self.shop.set_products, 'lalalal')
        self.assertRaises(ValueError, self.shop.set_products, [Product(1, 25)])

    def test_get_products(self):
        self.shop = Shop([Product("b", 25), Product("a", 25)])
        self.assertEqual(self.shop.get_products(), [Product("b", 25),
                                                    Product("a", 25)])

    def test_get_sorted_by_price(self):
        self.shop = Shop([Product("b", 25), Product("a", 125)])
        self.assertEqual(self.shop.get_sorted_by_price(), [Product("b", 25),
                                                           Product("a", 125)])

    def test_get_most_expensive_product(self):
        self.shop = Shop([Product("b", 125), Product("a", 25)])
        self.assertEqual(self.shop.get_most_expensive_product(), Product("b", 125))


if __name__ == '__main__':
    unittest.main()
