"""
What Is a List?

A list is a collection of items in a particular order. You can make a list that 
includes the letters of the alphabet, the digits from 0–9, or the names of 
all the people in your family
"""

bicycles = ['trek', 'cannondale', 'redline', 'specializaed']
print(bicycles)

# Accessing Elements in a List
bicycles = ['trek', 'cannondale', 'redline', 'specializaed']
print(bicycles[0])
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]) # By asking for the item at index -1, Python always returns the last item in the list

# Using Individual Values from a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
