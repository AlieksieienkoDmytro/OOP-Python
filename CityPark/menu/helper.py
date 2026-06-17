import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def press_q_to_continue():

    while True:
        choice = input("\nQ - zurück: ").upper()

        match choice:
            case "Q":
                clear_screen()
                return
            case _:
                print("\nUngültige Eingabe.")
