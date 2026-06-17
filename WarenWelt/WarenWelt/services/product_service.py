from models.products.buch import Buch
from models.products.elektronik import Elektronik
from models.products.kleidung import Kleidung


class ProductService:

    @staticmethod
    def load_all_products(storage):

        products = []

        products.extend(Buch.load_all(storage))
        products.extend(Elektronik.load_all(storage))
        products.extend(Kleidung.load_all(storage))

        return products

    @staticmethod
    def load_books(storage):
        return Buch.load_all(storage)

    @staticmethod
    def load_electronics(storage):
        return Elektronik.load_all(storage)

    @staticmethod
    def load_clothing(storage):
        return Kleidung.load_all(storage)