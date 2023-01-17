"""
5.2 More Conditional Tests

You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:

•	 Tests for equality and inequality with strings
•	 Tests using the lower() function
•	 Numerical tests involving equality and inequality, greater than and
     less than, greater than or equal to, and less than or equal to
•	 Tests using the and keyword and the or keyword
•	 Test whether an item is in a list
•	 Test whether an item is not in a list
"""

# Test for equality and inequality with strings
from traceback import print_tb


name = 'Alonso'
if name == 'Alonso':
    print('Wellcome back, Alonso')
else:
    print('You are not Alonso')

programming_language = 'java'
if programming_language != 'python':
    print('Python is more easy to learn')

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
if age != 18:
    print("")

# Test using the and keyword ant the or keyword

# Test whether an item is in a list

# Test whether an item is not in a list