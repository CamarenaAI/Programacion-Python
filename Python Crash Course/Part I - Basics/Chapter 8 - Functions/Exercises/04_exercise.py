def make_shirt(size, text):
    """Display information about the t-shirt."""
    print("The size of the t-shirt is: " + size)
    print("The text on the shirt reads: " + text.title()+ "\n")

make_shirt(size='small', text='i love python')
make_shirt(size='medium', text='python world')
make_shirt(size='large', text='pythoner')