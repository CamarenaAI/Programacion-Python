def make_shirt(size, text):
    """Display information about the t-shirt."""
    print(f"The size of the t-shirt is: {size}")
    print(f"The text on the shirt reads: {text.title()}")

make_shirt(size='large', text='python world')