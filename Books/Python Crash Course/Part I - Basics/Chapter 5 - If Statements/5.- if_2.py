# Conditional Test

# Checking for Equality
car = 'audi' # Insert the model of the car
if car == 'bmw':
	print(True)
else:
	print(False)

# Ignoring Case When Checking for Equality
car = 'Audi' # Insert the model of the car
if car.lower() == 'audi':
	print(True)
else:
	print(False)
print(car)

# Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Numerical Comparisons
age = 18
if age == 18:
    print(True)
else:
    print(False)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
if age < 21:
    print(True)
else:
    print(False)
if age <= 21:
    print(True)
else:
    print(False)
if age > 21:
    print(True)
else:
    print(False)
if age >= 21:
    print(True)
else:
    print(False)

# Checking Multiple Conditions
# Using and to Check Multiple Conditions
age_0 = 22 
age_1 = 22
if age_0 >= 21 and age_1 >= 21:
    print(True)
else:
    print(False)