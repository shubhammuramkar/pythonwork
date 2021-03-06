# ___________method 3___________
class Car():
	def __init__(self,make ,model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 500

	def get_descriptive_name(self):
		lon = str(self.year) + ' ' + self.make + " " + self.model
		return lon.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self,milages):
		if milages >= self.odometer_reading:
			self.odometer_reading = milages
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		print("New Miles :")
		self.odometer_reading += miles
"""Add the given amount to the odometer reading."""

class  Battery():
    """docstring for  Battery"""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            rang = 240
        elif self.battery_size == 80:
            rang = 270
        message = "This car can go approximately " + str(rang)
        message += " miles on a full charge."
        print(message)





class  ElectricCar(Car):
    """docstring for  ElectricCar"""
    def __init__(self, make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 80
        self.battery = Battery()   # instance of battery is made





my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
