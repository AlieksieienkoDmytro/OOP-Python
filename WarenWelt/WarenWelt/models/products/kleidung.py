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


    def save(self, storage):

        query = """
        INSERT INTO kleidung (name, price, weight, size, color)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            self.get_name(),
            self.get_price(),
            self.get_weight(),
            self.get_size(),
            self.get_color()
        )

        product_id = storage.execute_query(
            query,
            values
        )

        self.set_id(product_id)



    @staticmethod
    def load(storage, product_id):

        query = """
        SELECT *
        FROM kleidung
        WHERE id = %s
        """

        result = storage.fetch_query(
            query,
            (product_id,)
        )

        if not result:
            return None

        row = result[0]

        clothing = Kleidung(
            row['name'],
            row['price'],
            row['weight'],
            row['size'],
            row['color']
        )

        clothing.set_id(row['id'])

        return clothing


    @staticmethod
    def load_all(storage):

        query = """
        SELECT *
        FROM kleidung
        """

        result = storage.fetch_query(query)

        clothings = []

        for row in result:
            clothing = Kleidung(
                row['name'],
                row['price'],
                row['weight'],
                row['size'],
                row['color']
            )

            clothing.set_id(row['id'])

            clothings.append(clothing)

        return clothings