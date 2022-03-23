import csv

class Item:
  pay_rate = .8
  all = []
  def __init__(self, name: str, price: float, quantity=0):
    assert price >= 0, f"Price {price} is not greater than zero"
    assert quantity >= 0, f"Quantity {quantity} is not greater than zero"
    
    self.name = name
    self.price = price
    self.quantity = quantity

    Item.all.append(self)

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate

  # @classmethod
  # def instantiate_from_csv(cls):
  #   with open('items.csv', 'r') as f:
  #     reader = csv.DictReader(f)
  #     items = list(reader)
    
  #   for item in items:
  #     Item(
  #       name=item.get('name'),
  #       price=float(item.get('price')),
  #       quantity=int(item.get('quantity'))
  #     )
  
  @staticmethod
  def is_integeer(num):
    if isinstance(num, float):
      return num.is_integer()
    elif isinstance(num, int):
      return True
    else:
      return False

  def __repr__(self):
      return f"Item('{self.name}', {self.price}, {self.quantity})"

print(Item.is_integeer(7))
# Item.instantiate_from_csv()
# print(Item.all)
# item1 = Item("Phone", 100, 1)
# item1.apply_discount()

# item2 = Item("Laptop", 1000,3)
# item2.pay_rate = 0.7
# item2.apply_discount()

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)
