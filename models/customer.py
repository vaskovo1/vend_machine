from models.item import Item
from models.vending_machine import VendingMachine
from typing import Union


class Customer:
    def __init__(self, vm: VendingMachine):
        self.vm = vm

    def select_product(self) -> Union[Item, None]:
        codes_list = self.vm.return_available_products_by_code()
        product = None
        while product is None and not self.vm.is_empty():
            try:
                product_number = int(input(f"Please press one of {codes_list}  buttons or press 0 to leave: "))
            except ValueError:
                print(f"Please press one of {codes_list}  buttons or press 0 to leave: ")
            else:
                if product_number in codes_list:
                    return self.vm.find_item_by_code(product_number)
                elif product_number == 0:
                    return None

    def add_cash(self, money: float):
        self.vm.add_cash(money)
