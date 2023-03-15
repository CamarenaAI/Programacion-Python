# Tuples

# Defining a Tuple
"""
A tuple looks just like a list except you use parentheses instead of
square brackets. Once you define a tuple, you can access individual
elements by using each item’s index, just as you would for a list
"""

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

"""
dimensions = (200, 50)
dimensions[0] = 250

Traceback (most recent call last):
 File "dimensions.py", line 3, in <module>
 dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment
"""

# Looping Through All Values in a Tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension,"\n")

# Writing over a Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
 
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)