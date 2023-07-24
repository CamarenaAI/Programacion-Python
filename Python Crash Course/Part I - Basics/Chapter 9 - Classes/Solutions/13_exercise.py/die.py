from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        for value in range(10):
            print(f"The number is: {randint(1, self.sides)}")