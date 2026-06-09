from datetime import datetime
from models.customers.firmenkunde import Firmenkunde


class Bestellung:

    def __init__(self, cart):
        self.__customer = cart.get_customer()
        self.__products = cart.get_products().copy()
        self.__order_date = datetime.now()


    def get_customer(self):
        return self.__customer


    def get_products(self):
        return self.__products


    def get_order_date(self):
        return self.__order_date


    def calculate_total_amount(self):
        total_amount = 0

        for product in self.__products:
            total_amount += product.get_price()

        if isinstance(self.__customer, Firmenkunde):
            total_amount *= 0.95

        return round(total_amount, 2)


    def create_invoice(self, filename="invoice.txt"):
        with open(filename, "w", encoding="utf-8") as file:

            file.write("===== INVOICE =====\n\n")

            file.write(f"Order Date: {self.__order_date}\n")
            file.write(f"Customer: {self.__customer.get_name()}\n")
            file.write(f"Email: {self.__customer.get_email()}\n")
            file.write(f"Address: {self.__customer.get_address()}\n\n")

            file.write("Products:\n")

            for product in self.__products:
                file.write(
                    f"- {product.get_name()} | "
                    f"{product.get_price():.2f} EUR\n"
                )

            file.write("\n")

            if isinstance(self.__customer, Firmenkunde):
                file.write("Business Customer Discount: 5%\n")

            file.write(f"Total Amount: {self.calculate_total_amount():.2f} EUR\n")