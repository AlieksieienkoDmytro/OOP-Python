from kunde import Kunde
from validator import Validator

class PrivatKunde(Kunde):

    id_counter = 1

    def __init__(self, name, address, email, phone, password, birthdate):
        # Auto-increment mechanism for unique ID
        current_id = PrivatKunde.id_counter
        PrivatKunde.id_counter += 1

        # Passing the basic data to the constructor of the parent class (Kunde)
        super().__init__(current_id, name, address, email, phone, password)

        # Declare variables here because PyCharm wants them initialized inside __init__
        self.__birthdate = None

        self.set_birthdate(birthdate)


    def get_birthdate(self):
        return self.__birthdate


    def set_birthdate(self, birthdate):
        if not Validator.validate_birthdate(birthdate):
            raise ValueError(f"Ungültiges Geburtsdatum-Format: '{birthdate}'. Erwartet wird YYYY-MM-DD.")
        self.__birthdate = birthdate