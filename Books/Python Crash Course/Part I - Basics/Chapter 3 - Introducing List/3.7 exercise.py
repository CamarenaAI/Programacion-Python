"""
3.7 Shrinking Guest List

You just found out that your new dinner table won’t 
arrive in time for the dinner, and you have space for only two guests
•	Start with your program from Exercise 3-6. Add a new line that prints a 
    message saying that you can invite only two people for dinner
•	Use pop() to remove guests from your list one at a time until only two 
    names remain in your list. Each time you pop a name from your list, print 
    a message to that person letting them know you’re sorry you can’t invite 
    them to dinner
•	Print a message to each of the two people still on your list, letting them 
    know they’re still invited
•	Use del to remove the last two names from your list, so you have an empty 
    list. Print your list to make sure you actually have an empty list at the end 
    of your program
"""
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
