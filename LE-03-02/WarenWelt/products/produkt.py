from validator import Validator

class Produkt:
    def __init__(self, id, name, price, weight):
        self.__name = None
        self.__address = None
        self.__email = None
        self.__price = None
        self.__weight = None

        self.__id = id

        self.set_name(name)
        self.set_price(price)
        self.set_weight(weight)

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not Validator.validate_name(name):
            raise ValueError(f"Ungültiges Namensformat: '{name}'")
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if not Validator.validate_price(price):
            raise ValueError(f"Ungültiger Preis: '{price}'.")
        self.__price = float(price)

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        if not Validator.validate_weight(weight):
            raise ValueError(f"Ungültiges Gewicht: '{weight}'.")
        self.__weight = float(weight)