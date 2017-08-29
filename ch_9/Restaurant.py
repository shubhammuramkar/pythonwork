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

restaurant = Restaurant("Food Panda","veg")
# print("Restaurant Name is " + restaurant.restaurant_name)
# print("Food Type " + restaurant.cuisine_type)
restaurant.open_restaurant()
restaurant.describe_restaurant()



re = Restaurant("pizza hut","non veg")
re.open_restaurant()
re.describe_restaurant()


bot = Restaurant("Domino","Both")
bot.open_restaurant()
bot.describe_restaurant()



