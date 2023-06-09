sandwich_orders = ['jam', 'cheese', 'chicken', 'beef', 'shrimp', 'vegetarian']
finished_sandwiches = []

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()

    print(f"I made your {current_sandwiches} sandwich")
    finished_sandwiches.append(current_sandwiches)

print("\nThe following sandwiches have been finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())