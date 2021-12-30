from models.vending_machine import VendingMachine
from models.item import Item


class Merchant:
    def __init__(self, vm: VendingMachine):
        self.vm = vm

    def add_item(self, item: Item):
        self.vm.add_item(item)

    def remove_item(self, item: Item):
        self.vm.remove_item(item)
