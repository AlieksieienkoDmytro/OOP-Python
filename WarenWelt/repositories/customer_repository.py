class CustomerRepository:

    def __init__(self, storage):

        self.__storage = storage


    def save_privatkunde(self, privatkunde):

        query = """
        INSERT INTO privatkunde (name, address, email, phone, password, birthdate)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            privatkunde.get_name(),
            privatkunde.get_address(),
            privatkunde.get_email(),
            privatkunde.get_phone(),
            privatkunde.get_password(),
            privatkunde.get_birthdate()
        )

        customer_id = self.__storage.execute_query(
            query,
            values
        )

        privatkunde.set_id(customer_id)


    def save_firmenkunde(self, firmenkunde):

        query = """
        INSERT INTO firmenkunde (name, address, email, phone, password, company_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            firmenkunde.get_name(),
            firmenkunde.get_address(),
            firmenkunde.get_email(),
            firmenkunde.get_phone(),
            firmenkunde.get_password(),
            firmenkunde.get_company_id()
        )

        customer_id = self.__storage.execute_query(
            query,
            values
        )

        firmenkunde.set_id(customer_id)


    def load_privatkunde(self, customer_id):

        query = """
        SELECT *
        FROM privatkunde
        WHERE id = %s
        """

        return self.__storage.fetch_query(
            query,
            (customer_id,)
        )


    def load_firmenkunde(self, customer_id):

        query = """
        SELECT *
        FROM firmenkunde
        WHERE id = %s
        """

        return self.__storage.fetch_query(
            query,
            (customer_id,)
        )

    def load_all_privatkunden(self):
        query = """
        SELECT *
        FROM privatkunde
        """

        return self.__storage.fetch_query(query)


    def load_all_firmenkunden(self):
        query = """
        SELECT *
        FROM firmenkunde
        """

        return self.__storage.fetch_query(query)