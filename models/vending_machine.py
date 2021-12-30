import pandas as pd
from models.item import Item
from typing import Union


class VendingMachine:
    def __init__(self):

        self.items = []
        self.max_capacity = 20
        self.current_capacity = 0
        self.customer_balance = 0

    @staticmethod
    def hello_message():
        print("Welcome to our Vending Machine !")

    def show_items(self):
        if not self.is_empty():
            print('Products available:')
            print("-" * 20)
            for item in self.items:
                print(f"Button {item.code} --> {item.name:10} {item.price} $, {item.amount} in stock")
            print("-" * 20)
        else:
            print("There are no available products, please come again later")

    def find_item_by_code(self, item_code: int) -> Union[Item, None]:
        for item in self.items:
            if item.code == item_code:
                return item

    def buy_item(self, selected_product: Item):
        self.remove_item(selected_product)
        self.customer_balance -= selected_product.price
        self._update_current_capacity()
        print(f'You got {selected_product.name}')

    def remove_item(self, selected_product: Item):
        for item in self.items:
            if selected_product == item:
                if item.amount > 1:
                    item.amount -= 1
                else:
                    self.items.pop(self.items.index(selected_product))
            self._update_current_capacity()

    def add_item(self, item: Item):
        if self._is_full():
            print("There are no room for new snacks")
        else:
            self.items.append(item)
            # print(f"{item.amount} {item.name} added")
            self.current_capacity += item.amount

    def add_cash(self, money: float):
        if money <= 0.00:
            raise ValueError
        self.customer_balance = self.customer_balance + money
        print(f"Your balance is {self.customer_balance}$.")

    def _is_full(self) -> bool:
        return self.current_capacity == self.max_capacity

    def is_empty(self) -> bool:
        return self.current_capacity == 0

    def _update_current_capacity(self):
        self.current_capacity = 0
        for item in self.items:
            self.current_capacity += item.amount

    def is_enough_customer_balance(self, item_price) -> bool:
        return item_price <= self.customer_balance

    def return_change(self):
        if self.customer_balance > 0:
            print(f"{self.customer_balance} refunded.")
            self.customer_balance = 0
        print('Thank you, have a nice day!')

    def return_lists_of_available_product_codes(self) -> list:
        codes_list = []
        for item in self.items:
            codes_list.append(item.code)
        return codes_list

    @staticmethod
    def load_default_config() -> list:
        with open('config/default_config.csv', 'r') as default_config:
            return pd.read_csv(default_config).values.tolist()
