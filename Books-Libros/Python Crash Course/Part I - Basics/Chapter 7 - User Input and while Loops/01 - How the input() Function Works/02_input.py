# Using int() to Accept Numerical Input

age = input("How old are you? ")
age = int(age)
print(age >= 18)

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")