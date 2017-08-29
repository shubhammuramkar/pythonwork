class Car():
    def __init__(self,make ,model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        lon = str(self.year) + ' ' + self.make + " " + self.model
        return lon.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading :
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

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

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print("Udated battery size is ")
        return self.battery_size




class  ElectricCar(Car):
    """docstring for  ElectricCar"""
    def __init__(self, make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 80
        self.batter = Battery()   # instance of battery is made

    def update_battery_size(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")





my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.batter.describe_battery()
my_tesla.batter.get_range()
print(my_tesla.batter.upgrade_battery())

