from random import choice

class MyTicket():
    def __init__(self, my_ticket=[]):
        self.my_ticket = my_ticket

    def my_number(self, winning_number):
        self.my_lottery_number = []
        attempts = 0
        while len(self.my_lottery_number) < 4:
            pull_item = choice(my_ticket)

            if pull_item not in self.my_lottery_number:
                self.my_lottery_number.append(pull_item)
                attempts += 1

        while not self.has_common_characters(winning_number):
            self.my_lottery_number = []
            while len(self.my_lottery_number) < 4:
                pull_item = choice(my_ticket)

                if pull_item not in self.my_lottery_number:
                    self.my_lottery_number.append(pull_item)
                    attempts += 1

        return attempts

    def has_common_characters(self, winning_number):
        common_count = 0
        for item in self.my_lottery_number:
            if item in winning_number:
                common_count += 1
        return common_count == 4

    def generate_my_ticket(self, winning_number):
        print(f"My lottery number is: {self.my_lottery_number}")
        if self.has_common_characters(winning_number):
            print("Congratulations! You have a winning ticket.")
        else:
            print("Sorry, no luck this time.")

my_ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'q', 'w', 'e', 'r', 't', 'y']