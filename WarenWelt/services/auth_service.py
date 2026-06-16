from models.customers.privatkunde import PrivatKunde
from models.customers.firmenkunde import Firmenkunde
from exceptions.shop_error import ShopError

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


    @staticmethod
    def register_privatkunde(
            storage,
            name,
            address,
            email,
            phone,
            password,
            birthdate
    ):

        if PrivatKunde.load_by_email(storage, email):
            raise ShopError("E-Mail bereits vergeben.")

        customer = PrivatKunde(
            name,
            address,
            email,
            phone,
            password,
            birthdate
        )

        customer.save(storage)

        return customer

    @staticmethod
    def register_firmenkunde(
            storage,
            name,
            address,
            email,
            phone,
            password,
            company_id
    ):

        if Firmenkunde.load_by_email(storage, email):
            raise ShopError("E-Mail bereits vergeben.")

        customer = Firmenkunde(
            name,
            address,
            email,
            phone,
            password,
            company_id
        )

        customer.save(storage)

        return customer