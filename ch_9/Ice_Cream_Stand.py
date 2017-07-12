class Restaurant():
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		name = self.restaurant_name
		ty   = self.cuisine_type
		print("Restaurant Name " + name.title())
		print("Cuisine Type " + ty.title())

	def open_restaurant(self):
		print("Restaurant is open ")

class IceCreamStand(Restaurant):
	def flavors(self,flavors = ["Butterscoch","chocklate"]):
		print("List of Flavors are :")
		return flavors



obj = IceCreamStand("pizza hut","non veg")
obj.open_restaurant()
obj.describe_restaurant()
detail = obj.flavors()
print(detail)