from models.order import Bestellung


class OrderService:

    @staticmethod
    def create_order(cart):

        if len(cart.get_products()) == 0:
            return None

        order = Bestellung(cart)

        order.create_invoice()

        return order