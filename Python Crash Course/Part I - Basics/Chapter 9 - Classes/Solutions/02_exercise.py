class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.name} restaurant serves a {self.cuisine} cuisine")

    def open_restaurant(self):
        print(f"The restaurant is open. Come on in!")

restaurant = Restaurant('Osteria Francescana', 'italian')
restaurant.describe_restaurant()

restaurant = Restaurant('Pujol', 'mexican')
restaurant.describe_restaurant()

restaurant = Restaurant('Arpège', 'french')
restaurant.describe_restaurant()