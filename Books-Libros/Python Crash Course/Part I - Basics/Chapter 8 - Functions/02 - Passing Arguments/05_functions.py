# Avoiding Argument Errors

"""
def describe_pet(animal_type, pet_name):
    """"Display information about pet.""""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet()

TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
"""

def describe_pet(animal_type, pet_name):
    """Display information about pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='cat', pet_name='mr. cat')