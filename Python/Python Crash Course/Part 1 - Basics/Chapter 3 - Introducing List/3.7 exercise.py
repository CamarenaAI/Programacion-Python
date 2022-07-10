# 3.7 Shrinking Guest List
print("The Mr. Jeff Bezos can't come")
guests = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']
guests[2] = 'Steve Jobs'
guests.insert(0, 'Steve Wozniak')
guests.insert(4, 'Alan Turing')
guests.append('Elon Musk')

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

message_1 = "Hello " + guests[0] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1] + " \nI have a dinner in my house the next week, \nI would like you to come\n"

print(message_1)
print(message_2)

del guests[1]
del guests[0]
print(guests)