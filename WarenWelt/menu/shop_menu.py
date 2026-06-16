from models.cart import Warenkorb
from menu.products_menu import products_menu
from menu.cart_menu.cart_menu import cart_menu
from menu.order_menu import order_menu
from menu.helper import *


def shop_menu(storage, customer):

    cart = Warenkorb(customer)

    while True:
        clear_screen()
        print("\n===== SHOP =====")
        print("1. Produkte")
        print("2. Warenkorb")
        print("3. Bestellung")
        print("0. Logout")

        choice = input("\nAuswahl: ")

        match choice:

            case "1":
                products_menu(storage, cart)

            case "2":
                cart_menu(cart)

            case "3":
                order_menu(cart)

            case "0":
                return

            case _:
                print("\nUngültige Auswahl.")