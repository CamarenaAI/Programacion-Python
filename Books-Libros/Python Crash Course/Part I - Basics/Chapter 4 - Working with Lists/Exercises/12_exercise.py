"""
4.12 More Loops

All versions of foods.py in this section have avoided using for loops
when printing to save space. Choose a version of foods.py, and write two
for loops to print each list of foods
"""

# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for foods in my_foods:
    print("My favorite foods are:")
    print(foods)
for foods in friend_foods:
    print("\nMy friend's favorite foods are:")
    print(foods)