from products.produkt import Produkt
from validator import Validator

class Buch(Produkt):

    def __init__(self, name, price, weight, author, pages):
        # Declare variables here because PyCharm wants them initialized inside __init__
        self.__author = None
        self.__pages = None

        # Call parent constructor to store base attributes
        super().__init__(None, name, price, weight)

        # Storing data in instance variables
        self.set_author(author)
        self.set_pages(pages)


    def get_author(self):
        return self.__author


    def set_author(self, author):
        if not Validator.validate_author(author):
            raise ValueError(f"Ungültiges Autorenformat: '{author}'")
        self.__author = author


    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        if not Validator.validate_pages(pages):
            raise ValueError(f"Ungültige Seitenanzahl: '{pages}'")
        self.__pages = int(pages)