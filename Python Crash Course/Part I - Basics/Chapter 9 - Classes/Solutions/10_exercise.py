import module.restaurant as restaurant

restaurant = restaurant.Restaurant('express food', 'fast food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"\nNumber of customers served: {restaurant.number_served}")
restaurant.number_served = 5
print(f"Number of customers served: {restaurant.number_served}")
restaurant.set_number_served(10)
print(f"Number of customers served: {restaurant.number_served}")
restaurant.increment_number_served(2)
print(f"Number of customers served: {restaurant.number_served}")