sandwich_orders = ['pastrami', 'jam', 'cheese', 'chicken', 'pastrami', 
                'beef', 'shrimp', 'vegetarian', 'pastrami']
finished_sandwiches = []

print("The deli has run of pastrami")
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    current_sandwiches = sandwich_orders.pop()

    print("I made your " + current_sandwiches + " sandwich")
    finished_sandwiches.append(current_sandwiches)

finished_sandwiches.insert(0, 'pastrami')
print("\nThe following sandwiches have been finished:")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())