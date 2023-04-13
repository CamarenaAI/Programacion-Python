"""
7.4 Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings
until they enter a 'quit' value. As they enter each topping, print a
message saying you'll add that topping to their pizza
"""

prompt = "\nPlease enter a series of pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print("You'll add " + toppings.lower() + " to their pizza!")