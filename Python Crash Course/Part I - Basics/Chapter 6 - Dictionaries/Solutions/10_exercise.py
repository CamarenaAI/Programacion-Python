people_numbers = {
    'paul': [1, 9, 15],
    'john': [13, 128],
    'sarah': [26],
    'stephanie': [22, 90, 108, 224],
    'axel': [2, 7],
}

for name, numbers in people_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t {number}")