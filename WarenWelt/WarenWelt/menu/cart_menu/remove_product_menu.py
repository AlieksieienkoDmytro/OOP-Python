from services.cart_service import CartService

def remove_product_menu(cart):

    products = list(cart.get_products().keys())

    print("\n===== PRODUKT ENTFERNEN =====")

    for i, (product,quantity) in enumerate(cart.get_products().items(),start=1):
        print(
            f"{i}. "
            f"{product.get_name()} "
            f"x{quantity}"
        )

    choice = int(input("\nProduktnummer: "))

    selected_product = products[choice - 1]

    CartService.remove_product(cart, selected_product)