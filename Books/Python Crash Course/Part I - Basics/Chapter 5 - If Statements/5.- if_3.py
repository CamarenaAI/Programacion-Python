# if Statements

# Simple if Statements
age = 19
if age >= 18:
	print("You are old enough to vote")

age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")

# if-else Statements
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else: 
	print("Sorry, you are too younger to vote")
	print("Please register to vote as soon as you turn 18!")

# The if-elif-else Chain
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# Using Multiple elif Blocks
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
print("Your admission cost is $" + str(price) + ".")

# Omitting the else Block
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5
print("Your admission cost is $" + str(price) + ".")

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
