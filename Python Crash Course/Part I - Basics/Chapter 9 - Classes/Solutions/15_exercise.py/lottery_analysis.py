from lottery_number import Lottery
from my_ticket import MyTicket

lottery = Lottery()
lottery.number()
winning_number = lottery.winning_number
print(f"Winning number is: {winning_number}")

my_ticket_instance = MyTicket()
attempts = my_ticket_instance.my_number(winning_number)
my_ticket_instance.generate_my_ticket(winning_number)
print(f"Number of attempts: {attempts}")