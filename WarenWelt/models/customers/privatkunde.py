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


    def save(self, storage):

        query = """
        INSERT INTO privatkunde (name, address, email, phone, password, birthdate)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            self.get_name(),
            self.get_address(),
            self.get_email(),
            self.get_phone(),
            self.get_password(),
            self.get_birthdate()
        )

        customer_id = storage.execute_query(
            query,
            values
        )

        self.set_id(customer_id)

    @staticmethod
    def load(storage, customer_id):

        query = """
        SELECT *
        FROM privatkunde
        WHERE id = %s
        """

        result = storage.fetch_query(
            query,
            (customer_id,)
        )

        if not result:
            return None

        row = result[0]

        customer = PrivatKunde(
            row["name"],
            row["address"],
            row["email"],
            row["phone"],
            row["password"],
            str(row["birthdate"])
        )

        customer.set_id(row["id"])

        return customer

    @staticmethod
    def load_all(storage):

        query = """
        SELECT *
        FROM privatkunde
        """

        results = storage.fetch_query(query)

        customers = []

        for row in results:
            customer = PrivatKunde(
                row["name"],
                row["address"],
                row["email"],
                row["phone"],
                row["password"],
                str(row["birthdate"])
            )

            customer.set_id(row["id"])

            customers.append(customer)

        return customers