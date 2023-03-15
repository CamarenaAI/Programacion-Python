# Making Numerical Lists

# Using the range() function
for value in range(1,5): # Python’s range() function makes it easy to generate a series of numbers
    print(value)
print("\n")

for value in range(1,6):
    print(value)
print("\n")

# Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2)) 
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares, "\n")

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits), "\n")

# List Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)