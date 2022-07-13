"""
3.5 Changing Guest List

You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
•	Start with your program from Exercise 3-4. Add a print statement at the 
    end of your program stating the name of the guest who can’t make it.
•	Modify your list, replacing the name of the guest who can’t make it with 
    the name of the new person you are inviting.
•	Print a second set of invitation messages, one for each person who is still 
    in your list.
"""
print("The Mr. Jeff Bezos can't come")
guests = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']
guests[2] = 'Steve Jobs'


message_1 = "Hello Mr." + guests[0] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_3 = "Hello "  + guests[2] + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"

print(message_1)
print(message_2)
print(message_3)
