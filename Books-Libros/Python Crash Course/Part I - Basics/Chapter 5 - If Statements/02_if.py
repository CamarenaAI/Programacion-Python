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
if age_0 >= 21 and age_1 >= 21: # It is necessary to meet the 2 conditions
    print(True)
else:
    print(False)

# Using or to Check Multiple Conditions
age_0 = 10 
age_1 = 22
if age_0 >= 21 or age_1 >= 21: # It is necessary to meet 1 condition
    print(True)
else:
    print(False)

# Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
print(True)
'pepperoni' in requested_toppings
print(False)

# Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# Boolean Expressions
"""
A Boolean expression is just another name for a 
conditional test. A Boolean value is either True or False, just like the value 
of a conditional expression after it has been evaluated
"""
game_active = True
can_edit = False