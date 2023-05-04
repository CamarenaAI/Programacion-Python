print("The Mr. Jeff Bezos can't come")

guests = ['bill gates', 'marck zuckerberg', 'jeff bezos']
guests[2] = 'steve jobs'

message_1 = "Hello Mr." + guests[0].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1].title() + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_3 = "Hello "  + guests[2].title() + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"

print(message_1)
print(message_2)
print(message_3)