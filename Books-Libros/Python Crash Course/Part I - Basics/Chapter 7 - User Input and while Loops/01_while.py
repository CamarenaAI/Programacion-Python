# Introducing while Loops

# The while Loop in Action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    # print(message)

    if message != 'quit':
        print(message)

# Using a Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Using a break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go " + city.title() + "!")

# Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding Infinite Loops
x = 1
while x <= 5:
    print(x)
    x += 1

# This loop runs forever!
x = 1
while x <= 5:
    print(x)