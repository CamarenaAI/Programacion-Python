"""
6.1 Person

Use a dictionary to store information about a person you know. Store
their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print
each piece of information stored in your dictionary
"""

people = {
    'first_name': 'mark',
    'last_name': 'zuckerber',
    'age': 38,
    'city': 'white plains',
    }

print(people['first_name'].title() + " " + people['last_name'].title() +
    " live in " + people['city'].title() + " and He is " + 
    str(people['age']) + " years")