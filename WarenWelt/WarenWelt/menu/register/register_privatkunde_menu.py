from menu.helper import press_q_to_continue
from services.auth_service import AuthService
from exceptions.shop_error import ShopError


def register_privatkunde_menu(storage):

    try:

        print("\n===== PRIVATKUNDE =====")

        name = input("Name: ")
        address = input("Adresse: ")
        email = input("E-Mail: ")
        phone = input("Telefon: ")

        password = input("Passwort: ")
        password_repeat = input("Passwort wiederholen: ")

        if password != password_repeat:
            print("\nPasswörter stimmen nicht überein.")
            return

        birthdate = input("Geburtsdatum: ")

        AuthService.register_privatkunde(
            storage,
            name,
            address,
            email,
            phone,
            password,
            birthdate
        )

        print("\nRegistrierung erfolgreich.")

    except ShopError as e:
        print(f"\nFehler: {e}")

    press_q_to_continue()