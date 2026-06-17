from menu.helper import *
from models.order import Bestellung
from menu.cart_menu.remove_product_menu import remove_product_menu


def cart_menu(cart):

    while True:

        clear_screen()
        print("\n===== WARENKORB =====")

        products = cart.get_products()

        if not products:
            print("\nWarenkorb ist leer.")
            press_q_to_continue()
            return

        for product, quantity in products.items():
            print(
            f"{product.get_name()} "
            f"x{quantity}"
            )

        order = Bestellung(cart)

        print(
            f"\nGesamt: "
            f"{order.calculate_total_amount():.2f} EUR"
        )

        print("\n1. Produkt entfernen")
        print("0. Zurück")

        choice = input("\nAuswahl: ")

        match choice:

            case "1":
                remove_product_menu(cart)

            case "0":
                return

            case _:
                print("\nUngültige Auswahl.")