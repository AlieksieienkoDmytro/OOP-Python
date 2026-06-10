from models.customers.privatkunde import PrivatKunde
from models.customers.firmenkunde import Firmenkunde

class AuthService:

    @staticmethod
    def login(storage, email, password):

        customer = PrivatKunde.load_by_email(storage, email)

        if customer and customer.get_password() == password:
            return customer

        customer = Firmenkunde.load_by_email(storage, email)

        if customer and customer.get_password() == password:
            return customer

        return None