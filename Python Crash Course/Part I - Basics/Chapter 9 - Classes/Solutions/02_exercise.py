class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name.title()
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves a {self.cuisine} cuisine")

    def open_restaurant(self):
        print(f"The restaurant is open. Come on in!")

restaurant = Restaurant('osteria francescana', 'italian')
restaurant.describe_restaurant()

restaurant = Restaurant('pujol', 'mexican')
restaurant.describe_restaurant()

restaurant = Restaurant('arpège', 'french')
restaurant.describe_restaurant()