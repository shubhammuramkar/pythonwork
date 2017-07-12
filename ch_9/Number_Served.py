class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 3

	def describe_restaurant(self):
		name = self.restaurant_name
		ty   = self.cuisine_type
		print("Restaurant Name " + name.title())
		print("Cuisine Type " + ty.title())

	def open_restaurant(self):
		print("Restaurant is open ")

	def set_number_served(self,num):
		if num >= self.number_served:
			self.number_served = num
		else :
			print("Sorry! Invalid")

	def  increment_number_served(self):
		print("There are " + str(self.number_served) + " people are present.")



re = Restaurant("Food Panda","veg")
re.open_restaurant()
re.describe_restaurant()
re.set_number_served(20)
re.increment_number_served()