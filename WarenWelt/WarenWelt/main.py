from database.storage import Storage
from menu.start_menu import start_menu


def main():

    print("=== ONLINE SHOP TEST ===\n")

    storage = Storage(
        "localhost",
        "root",
        # YOUR PASSWORD!!!
        "",
        "onlineshop"
    )

    storage.connect()

    try:

        start_menu(storage)

    finally:
        storage.disconnect()


if __name__ == "__main__":
    main()