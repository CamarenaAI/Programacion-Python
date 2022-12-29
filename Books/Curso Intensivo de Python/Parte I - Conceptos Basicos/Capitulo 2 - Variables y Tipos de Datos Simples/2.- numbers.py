# Numbers

# Integers
# You can add (+), subtract (-), multiply (*), and divide (/) integers in Python
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

# Python uses two multiplication symbols to represent exponents(**)
print(3 ** 2)
print(3 ** 3)
print(10 ** 6)

# Python supports the order of operations too, so you can use multiple operations in one expression
print(2 + 3 * 4)
print((2 + 3) * 4)

# Floats
print(0.1 + 0.1)
print(0.2 + 0.2) 
print(2 * 0.1) 
print(2 * 0.2 )

# Be aware that you can sometimes get an arbitrary number of decimal places in your answer
print(0.2 + 0.1)
print(3 * 0.1)

# Avoiding Type Errors with the str() Function
age = 23
message = "Happy " + str(age) + "rd Birthday" # You can do this by wrapping the variable in the str() function, which tells Python to represent non-string values as strings
print(message)
