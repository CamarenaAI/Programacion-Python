from random import choice

class Lottery():
    def __init__(self, lottery_number=[]):
        self.lottery_number = lottery_number

    def number(self):
        self.winning_number = []
        while len(self.winning_number) < 4:
            pull_item = choice(lottery_number)

            if pull_item not in self.winning_number:
                print(f"We a pulled a {pull_item}!")
                self.winning_number.append(pull_item)

    def winning_lottery(self):
        print(f"The winning number is: {self.winning_number}")

lottery_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'q', 'w', 'e', 'r', 't', 'y']