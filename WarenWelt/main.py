from database.storage import Storage
from models.customers.firmenkunde import Firmenkunde
from models.customers.privatkunde import PrivatKunde
from models.products.buch import Buch
from models.products.elektronik import Elektronik
from models.warenkorb import Warenkorb
from models.bestellung import Bestellung


def main():

    print("=== ONLINE SHOP TEST ===\n")

    storage = Storage(
        "localhost",
        "root",
        "Alieksieienko6887",
        "onlineshop"
    )

    storage.connect()

    try:

        # Load customer from database
        customer = PrivatKunde.load(storage,1)
        print("Customer loaded:")
        print(customer.get_name(), "\n")

        # Load products from database
        book = Buch.load(storage,1)
        laptop = Elektronik.load(storage,1)
        print("Products loaded:")
        print(book.get_name())
        print(laptop.get_name(), "\n")

        # Create shopping cart
        cart = Warenkorb(customer)
        cart.add_product(book)
        cart.add_product(laptop)
        print("Shopping cart created.")
        print(f"Cart total: {cart.calculate_total_amount():.2f} EUR\n")

        # Create order
        order = Bestellung(cart)
        print("Order created.")
        print(f"Order total: {order.calculate_total_amount():.2f} EUR\n")

        # Create invoice
        order.create_invoice()
        print("Invoice created successfully.")
        print("File: invoice.txt")

        """
        # COMPANY
        # Load customer from database
        customer = Firmenkunde.load(storage, 1)
        print("Customer loaded:")
        print(customer.get_name(), "\n")

        # Load products from database
        book = Buch.load(storage, 1)
        laptop = Elektronik.load(storage, 1)
        print("Products loaded:")
        print(book.get_name())
        print(laptop.get_name(), "\n")

        # Create shopping cart
        cart = Warenkorb(customer)
        cart.add_product(book)
        cart.add_product(laptop)
        print("Shopping cart created.")
        print(f"Cart total: {cart.calculate_total_amount():.2f} EUR\n")

        # Create order
        order = Bestellung(cart)
        print("Order created.")
        print(f"Order total: {order.calculate_total_amount():.2f} EUR\n")

        # Create invoice
        order.create_invoice()
        print("Invoice created successfully.")
        print("File: invoice.txt")
        """

    finally:
        storage.disconnect()


if __name__ == "__main__":
    main()