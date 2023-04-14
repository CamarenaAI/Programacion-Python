# Tetsing Multiple Conditions

requested_toppings = ['mushrooms', 'extra chesse']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra chesse' in requested_toppings:
	print("Adding extra chesse.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'extra chesse']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
elif 'extra chesse' in requested_toppings:
	print("Adding extra chesse.")

print("\nFinished making your pizza!")