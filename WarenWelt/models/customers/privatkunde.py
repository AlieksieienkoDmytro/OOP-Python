from models.customers.kunde import Kunde
from database.validator import Validator
from exceptions.shop_error import ShopError


class PrivatKunde(Kunde):


    def __init__(self, name, address, email, phone, password, birthdate):
        # Passing the basic data to the constructor of the parent class (Kunde)
        super().__init__(None, name, address, email, phone, password)

        # Declare variables here because PyCharm wants them initialized inside __init__
        self.__birthdate = None

        self.set_birthdate(birthdate)


    def get_birthdate(self):
        return self.__birthdate


    def set_birthdate(self, birthdate):
        if not Validator.validate_birthdate(birthdate):
            raise ShopError(f"Ungültiges Geburtsdatum-Format: '{birthdate}'. Erwartet wird YYYY-MM-DD.")
        self.__birthdate = birthdate