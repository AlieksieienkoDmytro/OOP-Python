from database.validator import Validator
from menu.helper import clear_screen, press_q_to_continue
from services.product_service import ProductService
from services.cart_service import CartService


def products_menu(storage, cart):

    products = ProductService.load_all_products(storage)

    clear_screen()
    print("\n===== PRODUKTE =====")

    for i, product in enumerate(products,start=1):
        print(
            f"{i}. "
            f"{product.get_name()} - "
            f"{product.get_price():.2f} EUR"
        )

    choice = input("\nProdukt wählen (0 = zurück): ")

    if not Validator.validate_digits(choice):
        print("\nUngültige Auswahl.")
        press_q_to_continue()
        return

    choice = int(choice)

    if choice == 0:
        return

    if choice > len(products):
        print("\nUngültige Auswahl.")
        press_q_to_continue()
        return

    selected_product = products[choice - 1]

    quantity = input("Menge: ")

    if not Validator.validate_digits(quantity):
        print("\nUngültige Menge.")
        press_q_to_continue()
        return

    quantity = int(quantity)

    if quantity < 1 or quantity > 10:
        print("\nUngültige Menge.")
        press_q_to_continue()
        return

    CartService.add_product(cart, selected_product, quantity)

    print(
        f"\n{quantity}x "
        f"{selected_product.get_name()} "
        f"hinzugefügt."
    )

    press_q_to_continue()