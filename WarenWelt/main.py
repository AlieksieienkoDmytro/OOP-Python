from database.storage import Storage
from models.customers.privatkunde import PrivatKunde
from models.customers.firmenkunde import Firmenkunde
from models.products.elektronik import Elektronik
from models.products.buch import Buch
from exceptions.shop_error import ShopError
from repositories.customer_repository import CustomerRepository
from repositories.product_repository import ProductRepository


def main():
    print("=== START F1 SHOP SYSTEM ===\n")

    # Initialize database storage with credentials
    storage = Storage(
        host="localhost",
        user="root",
        # YOUR PASSWORD FROM DB!!!
        password="Alieksieienko6887",
        database="onlineshop"
    )

    customer_repository = CustomerRepository(storage)
    product_repository = ProductRepository(storage)

    # Establish connection to the database
    try:
        print("Verbindung zur Datenbank wird hergestellt...")
        storage.connect()
        print("Datenbankverbindung erfolgreich hergestellt.\n")
    except ShopError as error:
        print(f"Datenbankverbindung fehlgeschlagen: {error}")
        return

    # Creating Max Verstappen (PrivatKunde)
    try:
        max_v = PrivatKunde(
            name="Max Verstappen",
            address="Red Bull Ring Straße 1, 8724 Spielberg",
            email="max33@verstappen.nl",
            phone="+436643333333",
            password="Tutududu",
            birthdate="1997-09-30"
        )
        print("PrivatKunde (F1-Fahrer) wurde im Speicher erstellt.")

        # Saving Max Verstappen to the database
        print("PrivatKunde wird in der Datenbank gespeichert...")
        customer_repository.save_privatkunde(max_v)
        print("PrivatKunde erfolgreich in der Datenbank gespeichert.")

        # Displaying data including the newly generated database ID
        print(f"ID: {max_v.get_id()} | Name: {max_v.get_name()} | Geburtsdatum: {max_v.get_birthdate()}\n")
    except ShopError as error:
        print(f"Fehler beim Erstellen des Privatkunden: {error}\n")
    except ShopError as error:
        print(f"Datenbankfehler beim Speichern des Privatkunden: {error}\n")

    # Creating Red Bull Racing (Firmenkunde)
    try:
        rbr = Firmenkunde(
            name="Red Bull Racing GmbH",
            address="Bradbourne Drive, Milton Keynes, MK7 8BJ",
            email="info@redbullracing.com",
            phone="+441908279700",
            password="SimplyAndLovely",
            company_id="123456"
        )
        print("Firmenkunde (F1-Team) wurde im Speicher erstellt.")

        # Saving Red Bull Racing to the database
        print("Firmenkunde wird in der Datenbank gespeichert...")
        customer_repository.save_firmenkunde(rbr)
        print("Firmenkunde erfolgreich in der Datenbank gespeichert.")

        # Displaying data including the newly generated database ID
        print(f"ID: {rbr.get_id()} | Name: {rbr.get_name()} | Firmennummer: {rbr.get_company_id()}\n")
    except ShopError as error:
        print(f"Fehler beim Erstellen des Firmenkunden: {error}\n")
    except ShopError as error:
        print(f"Datenbankfehler beim Speichern des Firmenkunden: {error}\n")

    # Creating MacBook Pro (Elektronik)
    try:
        laptop = Elektronik(
            name="MacBook Pro",
            price=2499.99,
            weight=1.6,
            brand="Apple",
            warranty_years=2
        )
        print("Elektronik (Laptop) wurde im Speicher erstellt.")

        # Saving MacBook Pro to the database
        print("Elektronik wird in der Datenbank gespeichert...")
        product_repository.save_elektronik(laptop)
        print("Elektronik erfolgreich in der Datenbank gespeichert.")

        # Displaying data including the newly generated database ID
        print(
            f"ID: {laptop.get_id()} | Name: {laptop.get_name()} | Preis: {laptop.get_price()} | Marke: {laptop.get_brand()}\n")
    except ShopError as error:
        print(f"Fehler beim Erstellen der Elektronik: {error}\n")
    except ShopError as error:
        print(f"Datenbankfehler beim Speichern der Elektronik: {error}\n")

    # Creating Python Book (Buch)
    try:
        book = Buch(
            name="Python Crash Course",
            price=35.00,
            weight=0.8,
            author="Eric Matthes",
            pages=544
        )
        print("Buch wurde im Speicher erstellt.")

        # Saving Book to the database
        print("Buch wird in der Datenbank gespeichert...")
        product_repository.save_buch(book)
        print("Buch erfolgreich in der Datenbank gespeichert.")

        # Displaying data including the newly generated database ID
        print(
            f"ID: {book.get_id()} | Name: {book.get_name()} | Autor: {book.get_author()} | Seiten: {book.get_pages()}\n")
    except ShopError as error:
        print(f"Fehler beim Erstellen des Buches: {error}\n")
    except ShopError as error:
        print(f"Datenbankfehler beim Speichern des Buches: {error}\n")

    print("=== TEST DATEN LADEN ===")

    # Test loading a single customer (adjust ID if needed)
    print("Lade Privatkunde mit ID 1...")
    customer = customer_repository.load_privatkunde(1)
    print(f"Geladener Kunde: {customer}\n")

    # Test loading all products from a category
    print("Lade alle Bücher...")
    books = product_repository.load_all_buecher()
    print(f"Alle Bücher: {books}\n")

    print("=== TESTVALIDIERUNG (ERWARTETE FEHLER) ===\n")

    # Testing validation with invalid email format
    try:
        bad_driver = PrivatKunde(
            name="Checo Perez",
            address="Guadalajara, Mexico",
            email="checo@@redbull.com",
            phone="+523311111111",
            password="111111111",
            birthdate="1990-01-26"
        )
    except ShopError as e:
        print(f"Erwarteter Fehler beim Erstellen des Privatkunden: {e}\n")

    # Disconnect from the database safely
    print("Datenbankverbindung wird geschlossen...")
    storage.disconnect()
    print("Datenbankverbindung geschlossen. === ENDE ===")


if __name__ == "__main__":
    main()