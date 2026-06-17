from menu.helper import press_q_to_continue
from services.auth_service import AuthService
from exceptions.shop_error import ShopError


def register_firmenkunde_menu(storage):

    try:

        print("\n===== FIRMENKUNDE =====")

        name = input("Firmenname: ")
        address = input("Adresse: ")
        email = input("E-Mail: ")
        phone = input("Telefon: ")

        password = input("Passwort: ")
        password_repeat = input("Passwort wiederholen: ")

        if password != password_repeat:
            print("\nPasswörter stimmen nicht überein.")
            return

        company_id = input("Firmennummer: ")

        AuthService.register_firmenkunde(
            storage,
            name,
            address,
            email,
            phone,
            password,
            company_id
        )

        print("\nRegistrierung erfolgreich.")

    except ShopError as e:
        print(f"\nFehler: {e}")

    press_q_to_continue()