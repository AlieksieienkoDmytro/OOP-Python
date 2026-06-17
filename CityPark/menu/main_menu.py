from menu.erfasse_fahrzeug import erfasse_fahrzeug
from menu.zeige_tarife import zeige_tarife
from menu.berechne_parkpreis import berechne_parkpreis
from menu.drucke_ticket import drucke_ticket
from models.tarif import Tarif
from menu.helper import *


def main_menu():

    fahrzeug = None
    selected_tarif = None
    parkdauer = None
    last_price = None

    tarife = Tarif.get_all_tarife()

    while True:

        clear_screen()

        print("\n===== CITYPARK =====")
        print("1. Fahrzeug erfassen")
        print("2. Tarife anzeigen")
        print("3. Parkpreis berechnen")
        print("4. Parkticket drucken")
        print("Q. Beenden")

        choice = input("\nAuswahl: ")

        match choice.upper():

            case "1":
                fahrzeug = erfasse_fahrzeug()

            case "2":
                zeige_tarife(tarife)
                press_q_to_continue()

            case "3":
                selected_tarif, parkdauer, last_price = berechne_parkpreis(fahrzeug, tarife)

            case "4":
                drucke_ticket(fahrzeug, selected_tarif, parkdauer, last_price)

            case "Q":
                print("\nProgramm beendet.")
                break