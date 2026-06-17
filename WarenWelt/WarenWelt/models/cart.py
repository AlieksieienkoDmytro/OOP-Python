class Warenkorb:

    def __init__(self, customer):
        self.__customer = customer
        self.__products = {}


    def get_customer(self):
        return self.__customer


    def get_products(self):
        return self.__products


    def add_product(self, product, quantity):
        if product in self.__products:
            self.__products[product] += quantity
        else:
            self.__products[product] = quantity

    def remove_product(self, product):
        if product in self.__products:
            self.__products[product] -= 1

            if self.__products[product] <= 0:
                del self.__products[product]


    def clear_cart(self):
        self.__products.clear()