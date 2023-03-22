"""
6.7 People

Start with the program you wrote for Exercise 6.1 (page 102). Make two
new dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people.
As you loop through the list, print everything you know about each 
person
"""

people_0 = {
    'first_name': 'mark',
    'last_name': 'zuckerber',
    'age': 38, 
    'city': 'white plains',
    }

people_1 = {
    'first_name': 'jeff',
    'last_name': 'bezos',
    'age': 59,
    'city': 'albuquerque',
    }

people_2 = {
    'first_name': 'bill',
    'last_name': 'gates',
    'age': 67,
    'city': 'seattle',
    }
    
people = [people_0, people_1, people_2]

for person in people:
    print(person)