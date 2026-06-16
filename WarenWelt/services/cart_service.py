from models.cart import Warenkorb


class CartService:

    @staticmethod
    def create_cart(customer):
        return Warenkorb(customer)

    @staticmethod
    def add_product(cart, product, quantity):
        cart.add_product(product, quantity)

    @staticmethod
    def remove_product(cart, product):
        cart.remove_product(product)