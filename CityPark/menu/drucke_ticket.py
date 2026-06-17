from menu.helper import press_q_to_continue
from models.parkticket import Parkticket


def drucke_ticket(fahrzeug, selected_tarif, parkdauer, last_price):

    if  fahrzeug is None or selected_tarif is None:
        print("\nBitte zuerst Fahrzeug erfassen und Preis berechnen")
        press_q_to_continue()
        return

    ticket = Parkticket(fahrzeug, selected_tarif, parkdauer, last_price)

    ticket.print_ticket()

    press_q_to_continue()