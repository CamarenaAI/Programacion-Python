class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name.title()
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine}")

    def open_restaurant(self):
        print(f"The restaurant is open. Come on in!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_served):
        self.number_served += increment_served