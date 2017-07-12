# ___________method 2___________
class Car():
	def __init__(self,make ,model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 10

	def get_descriptive_name(self):
		lon = str(self.year) + ' ' + self.make + " " + self.model
		return lon.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.\n")

	# def update_odometer(self,milages):
	# 	self.odometer_reading = milages
	def update_odometer(self,milages):
		if milages >= self.odometer_reading:
			self.odometer_reading = milages
		else:
			print("You can't roll back an odometer!")



my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(2)
my_new_car.read_odometer()



new = Car('bmw', 'x4', 2016)
print(new.get_descriptive_name())
new.update_odometer(20)
new.read_odometer()