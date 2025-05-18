#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0
        if self.total < 0:
            self.total = 0
        # Remove last added items (if any)
        if self.items:
            # Remove as many items as were in the last transaction
            # This assumes all items in last transaction were the same
            # (as per add_item logic)
            last_item = self.items[-1]
            while self.items and self.items[-1] == last_item:
                self.items.pop()
