from models.order import Bestellung
from menu.helper import press_q_to_continue


def order_menu(cart):

    if not cart.get_products():
        print("\nWarenkorb ist leer.")
        press_q_to_continue()
        return

    order = Bestellung(cart)

    order.create_invoice()

    print("\nBestellung erfolgreich erstellt.")
    print(
        f"Gesamtbetrag: "
        f"{order.calculate_total_amount():.2f} EUR"
    )

    cart.clear_cart()

    press_q_to_continue()