from menu.register.register_privatkunde_menu import register_privatkunde_menu
from menu.register.register_firmenkunde_menu import register_firmenkunde_menu
from menu.helper import *


def register_menu(storage):

    while True:
        clear_screen()
        print("\n===== REGISTRIERUNG =====")
        print("1. Privatkunde")
        print("2. Firmenkunde")
        print("0. Zurück")

        choice = input("\nAuswahl: ")

        match choice:

            case "1":
                register_privatkunde_menu(storage)
                break

            case "2":
                register_firmenkunde_menu(storage)
                break

            case "0":
                return

            case _:
                print("\nUngültige Auswahl.")