"""
6.8 Pets

Make several dictionaries, where the name of each dictionary is the name
of a pet. In each dictionary, include the kind of animal and the owner’s 
name. Store these dictionaries in a list called pets. Next, loop through
your list and as you do print everything you know about each pet
"""

simba = {
    'kind': 'dog',
    'owner': 'omar'
}

felix = {
    'kind': 'cat',
    'owner': 'alexa'
}

arizona = {
    'kind': 'fish',
    'owner': 'kevin'
}

pixie = {
    'kind': 'parrot',
    'owner': 'lili'
}

pets = [simba, felix, arizona, pixie]

for pet in pets:
    print(pet)