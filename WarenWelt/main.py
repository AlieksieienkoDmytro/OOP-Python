from database.storage import Storage
from models.customers.firmenkunde import Firmenkunde
from models.customers.privatkunde import PrivatKunde
from models.products.buch import Buch
from models.products.elektronik import Elektronik
from models.warenkorb import Warenkorb
from models.bestellung import Bestellung
from services.auth_service import AuthService
from services.product_service import ProductService


def main():

    print("=== ONLINE SHOP TEST ===\n")

    storage = Storage(
        "localhost",
        "root",
        # YOUR PASSWORD!!!
        "Alieksieienko6887",
        "onlineshop"
    )

    storage.connect()

    try:

        customer = AuthService.login(storage, "max@verstappen.com", "Password123")

        if customer:
            print(customer.get_name())
        else:
            print("Customer not found.")

        customer = AuthService.login(storage, "info@redbullracing.com", "Business123")

        if customer:
            print(customer.get_name())
        else:
            print("Customer not found.")

        customer = AuthService.register_privatkunde(
            storage,
            "Dmytro",
            "Teststrasse 1",
            "dmytro@test.at",
            "+436601234567",
            "123456",
            "2000-01-01"
        )

        print(customer.get_name())
        print(customer.get_id())

        products = ProductService.load_all_products(
            storage
        )

        for product in products:
            print(
                product.get_name(),
                product.get_price()
            )

    finally:
        storage.disconnect()


if __name__ == "__main__":
    main()