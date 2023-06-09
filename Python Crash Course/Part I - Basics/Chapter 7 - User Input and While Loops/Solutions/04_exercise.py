prompt = "\nPlease enter a series of pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"You'll add {toppings.lower()} to their pizza!")