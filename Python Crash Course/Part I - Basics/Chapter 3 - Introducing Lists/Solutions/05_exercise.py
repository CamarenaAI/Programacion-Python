guests = ['bill gates', 'marck zuckerberg', 'jeff bezos']
print(f"The Mr. {guests[2].title()} can't come\n")
guests[2] = 'steve jobs'

print(f"Hello Mr. {guests[0].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hi {guests[1].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hello {guests[2].title()} \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come")