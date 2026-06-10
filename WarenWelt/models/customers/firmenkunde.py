from models.customers.kunde import Kunde
from database.validator import Validator
from exceptions.shop_error import ShopError


class Firmenkunde(Kunde):


    def __init__(self, name, address, email, phone, password, company_id):

        super().__init__(None, name, address, email, phone, password)

        self.__company_id = None

        self.set_company_id(company_id)


    def get_company_id(self):
        return self.__company_id


    def set_company_id(self, company_id):
        if not Validator.validate_company_id(company_id):
            raise ShopError(f"Ungültiges Firmennummer-Format: '{company_id}'.")
        self.__company_id = company_id


    def save(self, storage):

        query = """
        INSERT INTO firmenkunde (name, address, email, phone, password, company_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            self.get_name(),
            self.get_address(),
            self.get_email(),
            self.get_phone(),
            self.get_password(),
            self.get_company_id()
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
        FROM firmenkunde
        WHERE id = %s
        """

        result = storage.fetch_query(
            query,
            (customer_id,)
        )

        if not result:
            return None

        row = result[0]

        customer = Firmenkunde(
            row['name'],
            row['address'],
            row['email'],
            row['phone'],
            row['password'],
            row['company_id']
        )

        customer.set_id(row['id'])

        return customer

    @staticmethod
    def load_all_firmenkunden(storage):

        query = """
        SELECT *
        FROM firmenkunde
        """

        results = storage.fetch_query(query)

        customers = []

        for row in results:
            customer = Firmenkunde(
                row['name'],
                row['address'],
                row['email'],
                row['phone'],
                row['password'],
                row['company_id']
            )

            customer.set_id(row['id'])

            customers.append(customer)

        return customers



    @staticmethod
    def load_by_email(storage, email):

        query = """
        SELECT *
        FROM firmenkunde
        WHERE email = %s
        """

        result = storage.fetch_query(
            query,
            (email,)
        )

        if not result:
            return None

        row = result[0]

        customer = Firmenkunde(
            row['name'],
            row['address'],
            row['email'],
            row['phone'],
            row['password'],
            row['company_id']
        )

        customer.set_id(row['id'])

        return customer