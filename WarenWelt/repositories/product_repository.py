class ProductRepository:

    def __init__(self, storage):

        self.__storage = storage


    def save_elektronik(self, elektronik):

        query = """
        INSERT INTO elektronik (name, price, weight, brand, warranty_years)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            elektronik.get_name(),
            elektronik.get_price(),
            elektronik.get_weight(),
            elektronik.get_brand(),
            elektronik.get_warranty_years()
        )

        product_id = self.__storage.execute_query(
            query,
            values
        )

        elektronik.set_id(product_id)


    def save_kleidung(self, kleidung):

        query = """
        INSERT INTO kleidung (name, price, weight, size, color)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            kleidung.get_name(),
            kleidung.get_price(),
            kleidung.get_weight(),
            kleidung.get_size(),
            kleidung.get_color()
        )

        product_id = self.__storage.execute_query(
            query,
            values
        )

        kleidung.set_id(product_id)


    def save_buch(self, buch):

        query = """
        INSERT INTO buch (name, price, weight, author, pages)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            buch.get_name(),
            buch.get_price(),
            buch.get_weight(),
            buch.get_author(),
            buch.get_pages()
        )

        product_id = self.__storage.execute_query(
            query,
            values
        )

        buch.set_id(product_id)


    def load_buch(self, book_id):

        query = """
        SELECT *
        FROM buch
        WHERE id = %s
        """

        result = self.__storage.fetch_query(
            query,
            (book_id,)
        )

        return result


    def load_elektronik(self, product_id):

        query = """
        SELECT *
        FROM elektronik
        WHERE id = %s
        """

        result = self.__storage.fetch_query(
            query,
            (product_id,)
        )

        return result


    def load_kleidung(self, product_id):

        query = """
        SELECT *
        FROM kleidung
        WHERE id = %s
        """

        result = self.__storage.fetch_query(
            query,
            (product_id,)
        )

        return result


    def load_all_buecher(self):

        query = """
        SELECT *
        FROM buch
        """

        return self.__storage.fetch_query(query)


    def load_all_elektronik(self):

        query = """
        SELECT *
        FROM elektronik
        """

        return self.__storage.fetch_query(query)


    def load_all_kleidung(self):

        query = """
        SELECT *
        FROM kleidung
        """

        return self.__storage.fetch_query(query)