from models.products.produkt import Produkt
from database.validator import Validator
from exceptions.shop_error import ShopError


class Elektronik(Produkt):

    def __init__(self, name, price, weight, brand, warranty_years):
        self.__brand = None
        self.__warranty_years = None

        super().__init__(None, name, price, weight)

        self.set_brand(brand)
        self.set_warranty_years(warranty_years)


    def get_brand(self):
        return self.__brand


    def set_brand(self, brand):
        if not Validator.validate_brand(brand):
            raise ShopError(f"Ungültiges Markenformat: '{brand}'")
        self.__brand = brand


    def get_warranty_years(self):
        return self.__warranty_years


    def set_warranty_years(self, warranty_years):
        if not Validator.validate_warranty(warranty_years):
            raise ShopError(f"Ungültige Garantiezeit: '{warranty_years}'")
        self.__warranty_years = int(warranty_years)


    def save(self, storage):

        query = """
        INSERT INTO elektronik (name, price, weight, brand, warranty_years)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            self.get_name(),
            self.get_price(),
            self.get_weight(),
            self.get_brand(),
            self.get_warranty_years()
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
        FROM elektronik
        WHERE id = %s
        """

        result = storage.fetch_query(
            query,
            (product_id,)
        )

        if not result:
            return None

        row = result[0]

        electronic = Elektronik(
            row["name"],
            row["price"],
            row["weight"],
            row["brand"],
            row["warranty_years"]
        )

        electronic.set_id(row["id"])

        return electronic


    @staticmethod
    def load_all(storage):

        query = """
        SELECT *
        FROM elektronik
        """

        results = storage.fetch_query(query)

        electronics = []

        for row in results:
            electronic = Elektronik(
                row["name"],
                row["price"],
                row["weight"],
                row["brand"],
                row["warranty_years"]
            )

            electronic.set_id(row["id"])

            electronics.append(electronic)

        return electronics