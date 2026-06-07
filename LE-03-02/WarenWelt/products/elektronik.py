from products.produkt import Produkt
from validator import Validator

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
            raise ValueError(f"Ungültiges Markenformat: '{brand}'")
        self.__brand = brand


    def get_warranty_years(self):
        return self.__warranty_years


    def set_warranty_years(self, warranty_years):
        if not Validator.validate_warranty(warranty_years):
            raise ValueError(f"Ungültige Garantiezeit: '{warranty_years}'")
        self.__warranty_years = int(warranty_years)