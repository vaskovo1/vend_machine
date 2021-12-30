from models.customer import Customer
from models.vending_machine import VendingMachine
from models.item import Item
from models.merchant import Merchant


def test_vm():
    vm = VendingMachine()
    vm.hello_message()

    merchant = Merchant(vm)
    customer = Customer(vm)

    products = vm.load_default_config()

    for product in products:
        merchant.add_item(Item(*product))

    while True:
        vm.show_items()
        selected_product = customer.select_product()
        if selected_product is None:
            vm.return_change()
            break
        else:
            print(f"You have selected {selected_product.name}")
            while vm.is_enough_customer_balance(selected_product.price) is False:
                try:
                    money = float(
                        input(f"Please refill {selected_product.price - vm.customer_balance}$: "))
                    customer.add_cash(money)
                except ValueError:
                    continue
            vm.buy_item(selected_product)


test_vm()
