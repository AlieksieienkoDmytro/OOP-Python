class Tarif:

    def __init__(self, name, base_price, price_per_hour):
        self.__name = name
        self.__base_price = base_price
        self.__price_per_hour = price_per_hour


    def get_name(self):
        return self.__name


    def get_base_price(self):
        return self.__base_price


    def get_price_per_hour(self):
        return self.__price_per_hour


    def calculate_price(self, parkdauer, fahrzeugfaktor):
        return (self.__base_price + self.__price_per_hour * parkdauer) * fahrzeugfaktor


    @staticmethod
    def get_all_tarife():
        return [
            Tarif("Standard", 2.00, 1.50),
            Tarif("Kurzpark", 1.00, 2.00),
            Tarif("Langzeit", 5.00, 1.00)
        ]