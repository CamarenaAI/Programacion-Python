"""
7.3 Multiples of ten
                                                                       |
Ask the user for a number, and the report whether the number is a
multiple of 10 or not
"""

number = input("Please insert a number: ")
number = int(number)

if number % 10 == 0:
    print("The number is a multiple of 10")
else:
    print("The number isn't a multiple of 10")