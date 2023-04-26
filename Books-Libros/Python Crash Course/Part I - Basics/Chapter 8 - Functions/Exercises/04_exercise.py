"""
8.4 Large Shirt

Modify the make_shirt() function so that shirts are large by default
with a message that reads I love Python. Make a large shirt and a medium
shirt with the default message, and a shirt of any size with a different
message
"""

def make_shirt(size, text):
    """Display information about the t-shirt."""
    print("The size of the t-shirt is: " + size)
    print("The text on the shirt reads: " + text.title()+ "\n")

make_shirt(size='small', text='i love python')
make_shirt(size='medium', text='python world')
make_shirt(size='large', text='pythoner')