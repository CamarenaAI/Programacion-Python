"""
5.2 More Conditional Tests

You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:

•	Tests for equality and inequality with strings
•	Tests using the lower() function
•	Numerical tests involving equality and inequality, greater than and
    less than, greater than or equal to, and less than or equal to
•	Tests using the and keyword and the or keyword
•	Test whether an item is in a list
•	Test whether an item is not in a list
"""

# Test for equality and inequality with strings
name = 'Alonso'
if name == 'Alonso':
    print('Wellcome back, Alonso')
else:
    print('You are not Alonso')

programming_language = 'java'
if programming_language != 'python':
    print('Python is more easy to learn')
else:
    print('Good choose')

# Test using the lower() function
country = 'MeXiCo'
if country.lower() == 'mexico':
    print('You are mexican')
else:
    print("Where are you from?")

# Numerical Test
age = 18
if age == 18:
    print(True)
else:
    print("You are not 18")

if age != 18:
    print("You are not 18")
else:
    print("You are 18")

# Test using the and keyword and the or keyword
name = 'Andres'
age = 18
if name == 'Gabriel' or age >= 18:
    print("Please come in")
else:
    print("You can't pass")

name = 'Andres'
age = 21
if name == 'Andres' and age >= 21:
    print("Please come in Mr. Andres")
else:
    print("You can't pass")

# Test whether an item is in a list
fruits = ['pinapple', 'apple', 'grape', 'pear']
if 'pinapple' in fruits:
    print(True)

# Test whether an item is not in a list
fruits = ['pinapple', 'apple', 'grape', 'pear']
fruit = 'guava'
if fruit not in fruits:
    print(fruit.title() + " is not in the list")