class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted description name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement shoowing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attemps to roll the odometer back.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attemp to model a battery for an electric car."""
    def __init__(self, battery_size=65):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the batery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Check if the battery can be upgrade"""
        if self.battery_size == 40:
            self.battery_size = 65
            print("Upgrading the battery")
        else:
            print("Battery can't be upgraded")

class ElectricCar(Car):
    """Represent asspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """ 
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()