class Warenkorb:

    def __init__(self, customer):
        self.__customer = customer
        self.__products = []


    def get_customer(self):
        return self.__customer


    def get_products(self):
        return self.__products


    def add_product(self, product):
        self.__products.append(product)


    def remove_product(self, product):
        if product in self.__products:
            self.__products.remove(product)


    def clear_cart(self):
        self.__products.clear()


    def calculate_total_amount(self):
        total_amount = 0

        for product in self.__products:
            total_amount += product.get_price()

        return round(total_amount, 2)