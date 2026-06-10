from abc import ABC
from database.validator import Validator
from exceptions.shop_error import ShopError

class Kunde(ABC):

    def __init__(self, id, name, address, email, phone, password):
        # Declare variables here because PyCharm wants them initialized inside __init__
        self.__name = None
        self.__address = None
        self.__email = None
        self.__phone = None
        self.__password = None

        self.__id = id

        # Storing data in instance variables
        self.set_name(name)
        self.set_address(address)
        self.set_email(email)
        self.set_phone(phone)
        self.set_password(password)


    def get_id(self):
        return self.__id


    def get_name(self):
        return self.__name


    def set_name(self, name):
        # Call validator
        if not Validator.validate_name(name):
            # If validation fails, close the program safely
            raise ShopError(f"Ungültiges Namensformat: '{name}'")
        self.__name = name


    def get_address(self):
        return self.__address


    def set_address(self, address):
        if not Validator.validate_address(address):
            raise ShopError(f"Ungültiges Adressformat: '{address}'")
        self.__address = address


    def get_email(self):
        return self.__email


    def set_email(self, email):
        if not Validator.validate_email(email):
            raise ShopError(f"Ungültiges E-Mail-Format: '{email}'")
        self.__email = email


    def get_phone(self):
        return self.__phone


    def set_phone(self, phone):
        if not Validator.validate_phone(phone):
            raise ShopError(f"Ungültiges Telefonnummer-Format: '{phone}'")
        self.__phone = phone


    def get_password(self):
        return self.__password


    def set_password(self, password):
        if len(password) < 6:
            raise ShopError("Passwort muss mindestens 6 Zeichen lang sein.")
        self.__password = password


    def set_id(self, new_id):
        self.__id = new_id