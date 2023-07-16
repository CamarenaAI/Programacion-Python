class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name.title()
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.name} serves a wonderful {self.cuisine}")

    def open_restaurant(self):
        print(f"The restaurant is open. Come on in!")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        for flavor in self.flavors:
            print(f"- {flavor.title()}" )

icecream = IceCreamStand('sweet tooth', 'ice cream')
icecream.flavors = ['vanilla', 'chocolate', 'lemon']

icecream.describe_restaurant()
icecream.show_flavors()