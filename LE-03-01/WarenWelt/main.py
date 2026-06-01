from privatkunde import PrivatKunde
from firmenkunde import Firmenkunde

def main():
    print("=== START F1 ===\n")

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
        print("PrivatKunde (F1 Driver) erstellt")
        print(f"ID: {max_v.get_id()} | Name: {max_v.get_name()} | Geburtsdatum: {max_v.get_birthdate()}\n")
    except ValueError as e:
        print(f"Fehler beim Erstellen des Privat Kunden: {e}")


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
        print("Firmenkunde (F1 Team) erstellt.")
        print(f"ID: {rbr.get_id()} | Name: {rbr.get_name()} | Company ID: {rbr.get_company_id()}")
    except ValueError as e:
        print(f"Fehler beim Erstellen des Firmen Kunden: {e}")


    print("\n=== TESTVALIDIERUNG (ERWARTETE FEHLER) ===\n")

    try:
        bad_driver = PrivatKunde(
            name="Checo Perez",
            address="Guadalajara, Mexico",
            email="checo@@redbull.com",
            phone="+523311111111",
            password="111111111",
            birthdate="1990-01-26"
        )
    except ValueError as e:
        print(f"Fehler beim Erstellen des Privat Kunden: {e}")

if __name__ == "__main__":
    main()