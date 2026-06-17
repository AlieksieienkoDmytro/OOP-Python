from models.motorrad import Motorrad
from models.pkw import PKW
from models.transporter import Transporter
from menu.helper import clear_screen, press_q_to_continue
from database.validator import Validator


def erfasse_fahrzeug():

    clear_screen()
    print("\n===== ERFASSE FAHRZEUG =====")

    kennzeichen = input("Kennzeichen: ")

    if not Validator.validate_kennzeichen(kennzeichen):
        print("\nUngültiges Kennzeichen.")
        press_q_to_continue()
        return None

    typ = input("Fahrzeugtyp (Motorrad/PKW/Transporter): ").strip()

    if not Validator.validate_fahrzeugtyp(typ):
        print("\nUngültiger Fahrzeugtyp.")
        press_q_to_continue()
        return None

    if typ == "Motorrad":
        print("\nMotorrad gespeichert.")
        press_q_to_continue()
        return Motorrad(kennzeichen)

    elif typ == "PKW":
        print("\nPKW gespeichert.")
        press_q_to_continue()
        return PKW(kennzeichen)

    elif typ == "Transporter":
        print("\nTransporter gespeichert.")
        press_q_to_continue()
        return Transporter(kennzeichen)

    print("\nFehler: Ungültiger Fahrzeugtyp.")
    press_q_to_continue()

    return None