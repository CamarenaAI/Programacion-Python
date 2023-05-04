# Exercise 3.4
guests = ['bill gates', 'marck zuckerberg', 'jeff bezos']

message_1 = "Hello Mr." + guests[0].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_3 = "Hello "  + guests[2].title() + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"

print(message_1)
print(message_2)
print(message_3)
print("Number of guests: ", len(guests))

# Exercise 3.5
print("The Mr. Jeff Bezos can't come")

guests = ['bill gates', 'marck zuckerberg', 'jeff bezos']
guests[2] = 'steve jobs'

message_1 = "Hello Mr." + guests[0].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_3 = "Hello "  + guests[2].title() + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"

print(message_1)
print(message_2)
print(message_3)
print("Number of guests: ", len(guests))

# Exercise 3.6
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
print("Number of guests: ", len(guests))

# Exercise 3.7
print("The Mr. Jeff Bezos can't come")

guests = ['bill gates', 'marck zuckerberg', 'jeff bezos']
guests[2] = 'steve jobs'
guests.insert(0, 'steve wozniak')
guests.insert(4, 'alan turing')
guests.append('elon musk')

print("Hello guys, I found a bigger dinner table\n")

print("Sorry guys, I can invite only two people for dinner\n")
first_guest = guests.pop(5)
print('Sorry Mr. ' + first_guest.title() + ' I can invite only two people')

second_guest = guests.pop(4)
print('Sorry Mr. ' + second_guest.title() + ' I can invite only two people')

third_guest = guests.pop(3)
print('Sorry Mr. ' + third_guest.title() + ' I can invite only two people')

fourth_guest = guests.pop(0)
print('Sorry Mr. ' + fourth_guest.title() + ' I can invite only two people\n')

message_1 = "Hello " + guests[0].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"

print(message_1)
print(message_2)

del guests[1]
del guests[0]
print(guests)
print("Number of guests: ", len(guests))