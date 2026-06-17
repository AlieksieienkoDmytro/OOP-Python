from menu.helper import *
from menu.zeige_tarife import zeige_tarife
from database.validator import Validator

def berechne_parkpreis(fahrzeug, tarife):

    clear_screen()
    print("\n===== BERECHNE PARKPREIS =====")

    if fahrzeug is None:
        print("\nBitte zuerst ein Fahrzeug erfassen.")
        press_q_to_continue()
        return None, None, None

    zeige_tarife(tarife)

    choice = input("\nTarif wählen: ")

    if not Validator.validate_tarif(choice, tarife):
        print("\nUngültige Auswahl.")
        press_q_to_continue()
        return None, None, None

    choice = int(choice)

    tarif = tarife[choice - 1]

    parkdauer = input("Parkdauer in Stunden: ")

    if not Validator.validate_parkdauer(parkdauer):
        print("\nUngültige Parkdauer.")
        press_q_to_continue()
        return None, None, None

    parkdauer = float(parkdauer)

    faktor = fahrzeug.get_faktor()

    preis = tarif.calculate_price(parkdauer, faktor)

    print(f"\nParkpreis: {preis:.2f} EUR")
    press_q_to_continue()

    return tarif, parkdauer, preis