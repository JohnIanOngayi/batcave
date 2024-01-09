#!/usr/bin/python3
import csv
class Item:
	pay_rate = 0.8
	all = []
	def __init__(self, name: str, price=0, quantity=1):
		print("Item: {0} initialised!".format(name))	
		#assert quantity >= 0 ,f"Item quantity for {name} must be greater than 0"
  
		self.name = name
		self.price = price
		self.quantity = quantity
		#Item.all.append(self)

	def calculate_total_price(self):
		return (self.quantity * self.price)

	def apply_discount(self):
		self.price = self.pay_rate * self.price

	def __repr__(self):
		return f"\nItem({self.name}, {self.price}, {self.quantity})\n"

	@classmethod
	def read_csv(cls):
		with open('/home/johnian/batcave/OOP/data.csv', 'r') as f:
			reader = csv.DictReader(f)
			items = list(reader)
			for item in items:
				Item(
				name=item.get('name'),
				price=item.get('price'),
				quantity= item.get('quantity')
				)
				Item.all.append(item)	
				#print(item)
        
'''
item1 = Item("HP Envy 2020", 1000, 5)
item2 = Item("Audi S8-L", 100000, 2)
item2.pay_rate = 0.75
item3 = Item("Toyota Crown Athlete", 100000)
item4 = Item(5, 100000)

item1.apply_discount()
item2.apply_discount()
item3.apply_discount()
item4.apply_discount()
'''

#print("{1} units of {0} cost {2}".format(item1.name, item1.quantity, (item1.calculate_total_price())))
#print("{1} units of {0} cost {2}".format(item2.name, item2.quantity, (item2.calculate_total_price())))
#print("{1} units of {0} cost {2}".format(item3.name, item3.quantity, (item3.calculate_total_price())))
#print("{1} units of {0} cost {2}".format(item4.name, item4.quantity, (item4.calculate_total_price())))
Item.read_csv()
print(Item.all)