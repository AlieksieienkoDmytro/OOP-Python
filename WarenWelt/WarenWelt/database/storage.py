import mysql.connector
from exceptions.shop_error import ShopError


class Storage:

    def __init__(self, host, user, password, database):
        # Declare variables here because PyCharm wants them initialized inside __init__
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

        # This will hold the active connection object
        self.__connection = None


    def connect(self):
        # Establish connection to the MySQL database
        try:
            self.__connection = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
        except mysql.connector.Error as error:
            # If connection fails, raise an error with the database message
            raise ShopError(f"Verbindung zur Datenbank fehlgeschlagen: {error}")


    def disconnect(self):
        # Close the connection safely if it is open
        if self.__connection and self.__connection.is_connected():
            self.__connection.close()


    def execute_query(self, query, values=None):

        try:
            with self.__connection.cursor() as cursor:

                cursor.execute(query, values)

                self.__connection.commit()

                return cursor.lastrowid

        except Exception as error:
            self.__connection.rollback()
            raise ShopError(f"Datenbankabfrage fehlgeschlagen: {error}")


    def fetch_query(self, query, values=None):

        try:
            with self.__connection.cursor(dictionary=True) as cursor:

                cursor.execute(query, values)

                return cursor.fetchall()

        except Exception as error:
            raise ShopError(f"Datenbankabfrage fehlgeschlagen: {error}")