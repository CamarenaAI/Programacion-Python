"""
6.10 Favorite Numbers

Modify your program from Exercise 6.2 (page 102) so each person can have
more than one favorite number. Then print each person’s name along with
their favorite numbers
"""

people_numbers = {
    'paul': [1, 9, 15],
    'john': [13, 128],
    'sarah': [26],
    'stephanie': [22, 90, 108, 224],
    'axel': [2, 7],
}

for name, numbers in people_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))