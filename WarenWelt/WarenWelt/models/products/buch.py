from models.products.produkt import Produkt
from database.validator import Validator
from exceptions.shop_error import ShopError


class Buch(Produkt):

    def __init__(self, name, price, weight, author, pages):
        # Declare variables here because PyCharm wants them initialized inside __init__
        self.__author = None
        self.__pages = None

        # Call parent constructor to store base attributes
        super().__init__(None, name, price, weight)

        # Storing data in instance variables
        self.set_author(author)
        self.set_pages(pages)


    def get_author(self):
        return self.__author


    def set_author(self, author):
        if not Validator.validate_author(author):
            raise ShopError(f"Ungültiges Autorenformat: '{author}'")
        self.__author = author


    def get_pages(self):
        return self.__pages


    def set_pages(self, pages):
        if not Validator.validate_pages(pages):
            raise ShopError(f"Ungültige Seitenanzahl: '{pages}'")
        self.__pages = int(pages)


    def save(self, storage):

        query = """
        INSERT INTO buch
        (name, price, weight, author, pages)
        VALUES
        (%s, %s, %s, %s, %s)
        """

        values = (
            self.get_name(),
            self.get_price(),
            self.get_weight(),
            self.get_author(),
            self.get_pages()
        )

        product_id = storage.execute_query(
            query,
            values
        )

        self.set_id(product_id)


    @staticmethod
    def load(storage, book_id):

        query = """
        SELECT *
        FROM buch
        WHERE id = %s
        """

        result = storage.fetch_query(
            query,
            (book_id,)
        )

        if not result:
            return None

        row = result[0]

        book = Buch(
            row['name'],
            row['price'],
            row['weight'],
            row['author'],
            row['pages']
        )

        book.set_id(row["id"])

        return book


    @staticmethod
    def load_all(storage):

        query = """
        SELECT *
        FROM buch
        """

        results = storage.fetch_query(query)

        books = []

        for row in results:
            book = Buch(
                row['name'],
                row['price'],
                row['weight'],
                row['author'],
                row['pages']
            )

            book.set_id(row["id"])

            books.append(book)

        return books