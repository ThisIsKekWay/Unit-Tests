from typing import List
from product import Product


class Shop:

    def validation(self, items) -> bool:
        if type(items) is not list:
            return False

        for item in items:
            if type(item) is Product or item.get_price() <= 0 or type(item.get_name()) is not str:
                return False
        return True

    def __init__(self, items: List[Product]):
        if items is not None and len(items) != 0:
            if self.validation(items):
                self.__products = items
            else:
                raise ValueError("Wrong data")
        else:
            raise ValueError("Empty data")

    def get_products(self):
        return self.__products

    def set_products(self, items: List[Product]):
        if items is not None and len(items) != 0:
            if self.validation(items):
                self.__products.append(items)
            else:
                raise ValueError("Wrong data")
        else:
            raise ValueError("Empty data")

    def get_sorted_by_price(self) -> List[Product]:
        return sorted(self.__products, key=lambda x: x.get_price())

    def get_most_expensive_product(self) -> Product:
        return max(self.__products, key=lambda x: x.get_price())
