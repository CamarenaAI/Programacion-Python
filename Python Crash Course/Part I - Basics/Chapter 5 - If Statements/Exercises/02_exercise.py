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