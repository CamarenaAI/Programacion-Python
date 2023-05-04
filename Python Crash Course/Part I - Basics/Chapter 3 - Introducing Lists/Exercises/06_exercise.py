print("The Mr. Jeff Bezos can't come")

guests = ['bill gates', 'marck zuckerberg', 'jeff bezos']
guests[2] = 'steve jobs'
guests.insert(0, 'steve wozniak')
guests.insert(4, 'alan turing')
guests.append('elon musk')

print("Hello guys, I found a bigger dinner table ")

message_1 = "Hello Mr." + guests[0].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_3 = "Hello "  + guests[2].title() + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"
message_4 = "Hello Mr." + guests[3].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_5 = "Hi " + guests[4].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_6 = "Hello "  + guests[5].title() + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"

print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)