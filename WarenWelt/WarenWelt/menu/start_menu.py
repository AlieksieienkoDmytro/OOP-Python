from menu.login_menu import login_menu
from menu.register.register_menu import register_menu
from menu.helper import clear_screen


def start_menu(storage):

    while True:
        clear_screen()
        print("\n===== WARENWELT =====")
        print("1. Login")
        print("2. Registrieren")
        print("0. Ende")

        choice = input("\nAuswahl: ")

        match choice:

            case "1":
                login_menu(storage)

            case "2":
                register_menu(storage)

            case "0":
                print("\nProgramm beendet.")
                break

            case _:
                pass