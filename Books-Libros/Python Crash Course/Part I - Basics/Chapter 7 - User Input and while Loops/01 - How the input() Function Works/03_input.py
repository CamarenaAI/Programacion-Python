# The Modulo Operator

print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

number = input("Enter a number, and I'll tell you it it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")