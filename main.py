from models.customer import Customer
from models.vending_machine import VendingMachine
from models.item import Item
from models.merchant import Merchant


def test_vm():
    self = VendingMachine()
    self.hello_message()

    merchant = Merchant(self)
    customer = Customer(self)

    products = self.load_default_config()

    for product in products:
        merchant.add_item(Item(*product))

    while True:
        self.show_items()
        selected_product = customer.select_product()
        if selected_product is None:
            self.return_change()
            break
        elif selected_product:
            print(f"You have selected {selected_product.name}")
            while self.is_enough_customer_balance(selected_product.price) is False:
                try:
                    money = float(
                        input(f"Please refill {selected_product.price - self.customer_balance}$: "))
                    customer.add_cash(money)
                except ValueError:
                    continue
            self.buy_item(selected_product)


test_vm()
