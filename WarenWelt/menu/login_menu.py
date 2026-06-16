from services.auth_service import AuthService
from menu.shop_menu import shop_menu
from menu.helper import *

def login_menu(storage):
    clear_screen()

    print("\n===== LOGIN =====")

    email = input("E-Mail: ")
    password = input("Passwort: ")

    customer = AuthService.login(storage, email, password)

    if customer is None:
        print("\nLogin fehlgeschlagen.")
        press_q_to_continue()
        return

    shop_menu(storage, customer)