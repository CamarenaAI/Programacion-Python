class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The {self.name} restaurant serves a {self.cuisine} cuisine")

    def open_restaurant(self):
        print(f"The restaurant is open. Come on in!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_served):
        self.number_served += increment_served

restaurant = Restaurant('Osteria Francescana', 'italian')
restaurant.describe_restaurant()

print(f"\nNumber of customers served: {restaurant.number_served}")
restaurant.number_served = 5
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(10)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(2)
print(f"Number of customers served: {restaurant.number_served}")