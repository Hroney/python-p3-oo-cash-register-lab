#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []
    pass

  def add_item(self, name, price, quantity=1):
    num = 0
    while num < quantity:
      self.items.append(name)
      num += 1
      self.lastItem = price * quantity
    self.total += price * quantity

  def apply_discount(self):
      self.total = int(self.total * (1 - 0.01 * self.discount))
      self.getvalue()

  def getvalue(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    self.total -= self.lastItem
    pass