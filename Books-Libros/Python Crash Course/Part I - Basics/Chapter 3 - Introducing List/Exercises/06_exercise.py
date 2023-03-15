"""
3.6 More Guest

You just found a bigger dinner table, so now more space is available.
Think of three more guests to invite to dinner
•	Start with your program from Exercise 3-4 or Exercise 3-5. Add a
    print statement to the end of your program informing people that you 
    found a bigger dinner table
•	Use insert() to add one new guest to the beginning of your list
•	Use insert() to add one new guest to the middle of your list
•	Use append() to add one new guest to the end of your list
•	Print a new set of invitation messages, one for each person in 
    your list
"""

print("The Mr. Jeff Bezos can't come")
guests = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']
guests[2] = 'Steve Jobs'
guests.insert(0, 'Steve Wozniak')
guests.insert(4, 'Alan Turing')
guests.append('Elon Musk')

print("Hello guys, I found a bigger dinner table ")

message_1 = "Hello Mr." + guests[0] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_3 = "Hello "  + guests[2] + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"
message_4 = "Hello Mr." + guests[3] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_5 = "Hi " + guests[4] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_6 = "Hello "  + guests[5] + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"

print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)