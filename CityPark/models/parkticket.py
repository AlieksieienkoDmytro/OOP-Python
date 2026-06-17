from datetime import datetime


class Parkticket:

    def __init__(self, fahrzeug, tarif, parkdauer, preis):
        self.__fahrzeug = fahrzeug
        self.__tarif = tarif
        self.__parkdauer = parkdauer
        self.__preis = preis
        self.__created_at = datetime.now()


    def print_ticket(self):
        print("\n===== PARKTICKET =====")
        print(f"Kennzeichen: {self.__fahrzeug.get_kennzeichen()}")
        print(f"Fahrzeugtyp: {self.__fahrzeug.get_typ()}")
        print(f"Tarif: {self.__tarif.get_name()}")
        print(f"Parkdauer: {self.__parkdauer} Stunden")
        print(f"Parkpreis: {self.__preis:.2f} EUR")
        print(f"Zeitstempel: {self.__created_at.strftime('%Y-%m-%d %H:%M')}")
        print("======================")