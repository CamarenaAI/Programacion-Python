prompt = "\n Please enter your age: "

while True:
    age = int(input(prompt))

    if age < 3:
        print("Your ticket is free")
    elif age >= 3 and age < 12:
        print("Your ticket cost is 10$")
    else:
        print("Your ticket cost is 12$")
    break