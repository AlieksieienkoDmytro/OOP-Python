from models.products.produkt import Produkt
from database.validator import Validator
from exceptions.shop_error import ShopError

class Kleidung(Produkt):

    def __init__(self, name, price, weight, size, color):
        self.__size = None
        self.__color = None

        super().__init__(None, name, price, weight)

        self.set_size(size)
        self.set_color(color)


    def get_size(self):
        return self.__size


    def set_size(self, size):
        if not Validator.validate_size(size):
            raise ShopError(f"Ungültiges Größenformat: '{size}'")
        self.__size = size


    def get_color(self):
        return self.__color


    def set_color(self, color):
        if not Validator.validate_color(color):
            raise ShopError(f"Ungültiges Farbformat: '{color}'")
        self.__color = color