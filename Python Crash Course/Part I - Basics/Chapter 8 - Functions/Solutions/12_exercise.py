def make_sandwich(*toppings):
    """Summarize the sandwich we are about to make."""
    print(f"\n Making a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('chicken', 'tomatoe', 'onion')
make_sandwich('beef', 'onion')
make_sandwich('tuna', 'tomatoe', 'pepper')