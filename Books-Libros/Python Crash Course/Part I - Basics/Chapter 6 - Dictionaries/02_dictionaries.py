# Working with Dictionaries

"""
A dictionary in Python is a collection of key-value pairs. Each key is
connected to a value, and you can use a key to access the value
associated with that key. A key's value can be a number a string a list,
or even another dictionary. In fact, you can use any object that you can
create in Python as a value in a dictionary.
In Python, a dictionary is wrapped in braces, {}, with a series of
key-value pairs inside the braces, as shown in the earlier example:

alien_0 = {'color': 'green', 'points': 5}

A key-value pairs is a set of values associated with each other. When
you provide a key, Python returns the value associated with that key.
Every key is connected to its value by a colon, and individual
key-value pairs are separated by commas. You can store as many key-value
pairs as you want in a dictionary.
The simplest dictionary has exactly one key-value pair, as shown in this 
modified version of the alien_0 dictionary:

alien_0 = {'color': 'green'}

This dictionary stores one piece of information about alien_0, namely
the alien’s color. The string 'color' is a key in this dictionary, and
its associated value is 'green'
"""

# Accessing Values in a Dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("You just earned" + str(new_points) + " points!")

# Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'color': 'yellow'}
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position " + str(alien_0['x_position']))
# move the alien to the right.
# determine how far to move the alien based on its current speed.
if alien_0['speed']  == 'slow':
    x_increment = 1
elif alien_0['speed']  == 'medium':
    x_increment = 2
else:
    # this must be a fast alien.
    x_increment = 3

# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# Removig Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# A Dictionary of Similar Obejcts
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")