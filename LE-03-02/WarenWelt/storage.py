import mysql.connector

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
            raise RuntimeError(f"Verbindung zur Datenbank fehlgeschlagen: {error}")


    def disconnect(self):
        # Close the connection safely if it is open
        if self.__connection and self.__connection.is_connected():
            self.__connection.close()


    def save_privatkunde(self, privatkunde):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO privatkunde (name, address, email, phone, password, birthdate) "
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    (
                        privatkunde.get_name(),
                        privatkunde.get_address(),
                        privatkunde.get_email(),
                        privatkunde.get_phone(),
                        privatkunde.get_password(),
                        privatkunde.get_birthdate()
                    )
                )
                self.__connection.commit()
                privatkunde.set_id(cursor.lastrowid)
        except Exception:
            self.__connection.rollback()
            raise


    def save_firmenkunde(self, firmenkunde):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO firmenkunde (name, address, email, phone, password, company_id) "
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    (
                        firmenkunde.get_name(),
                        firmenkunde.get_address(),
                        firmenkunde.get_email(),
                        firmenkunde.get_phone(),
                        firmenkunde.get_password(),
                        firmenkunde.get_company_id()
                    )
                )
                self.__connection.commit()
                firmenkunde.set_id(cursor.lastrowid)
        except Exception:
            self.__connection.rollback()
            raise


    def save_elektronik(self, elektronik):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO elektronik (name, price, weight, brand, warranty_years) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (
                        elektronik.get_name(),
                        elektronik.get_price(),
                        elektronik.get_weight(),
                        elektronik.get_brand(),
                        elektronik.get_warranty_years()
                    )
                )
                self.__connection.commit()
                elektronik.set_id(cursor.lastrowid)
        except Exception:
            self.__connection.rollback()
            raise


    def save_kleidung(self, kleidung):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO kleidung (name, price, weight, size, color) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (
                        kleidung.get_name(),
                        kleidung.get_price(),
                        kleidung.get_weight(),
                        kleidung.get_size(),
                        kleidung.get_color()
                    )
                )
                self.__connection.commit()
                kleidung.set_id(cursor.lastrowid)
        except Exception:
            self.__connection.rollback()
            raise


    def save_buch(self, buch):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO buch (name, price, weight, author, pages) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (
                        buch.get_name(),
                        buch.get_price(),
                        buch.get_weight(),
                        buch.get_author(),
                        buch.get_pages()
                    )
                )
                self.__connection.commit()
                buch.set_id(cursor.lastrowid)
        except Exception:
            self.__connection.rollback()
            raise

    def load_produkt(self, produkt_id, kategorie):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT * "
                    f"FROM {kategorie} "
                    f"WHERE id = %s",
                    (produkt_id,)
                )
                return cursor.fetchone()
        except Exception:
            raise

    def load_all_produkte(self, kategorie):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT * "
                    f"FROM {kategorie}"
                )
                return cursor.fetchall()
        except Exception:
            raise

    def load_kunde(self, kunden_id, kunden_typ):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT * "
                    f"FROM {kunden_typ} "
                    f"WHERE id = %s",
                    (kunden_id,)
                )
                return cursor.fetchone()
        except Exception:
            raise

    def load_all_kunden(self, kunden_typ):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT * "
                    f"FROM {kunden_typ}"
                )
                return cursor.fetchall()
        except Exception:
            raise