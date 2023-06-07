# Exercise 3.4
guests = ['bill gates', 'marck zuckerberg', 'jeff bezos']

print(f"Hello Mr. {guests[0].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hi {guests[1].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hello {guests[2].title()} \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come")
print("Number of guests: ", len(guests))

# Exercise 3.5
guests = ['bill gates', 'marck zuckerberg', 'jeff bezos']

print(f"Hello Mr. {guests[0].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hi {guests[1].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hello {guests[2].title()} \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come")
print("Number of guests: ", len(guests))

# Exercise 3.6
guests = ['bill gates', 'marck zuckerberg', 'jeff bezos']
print(f"The Mr. {guests[2].title()} can't come\n")
guests[2] = 'steve jobs'
guests.insert(0, 'steve wozniak')
guests.insert(4, 'alan turing')
guests.append('elon musk')

print("Hello guys, I found a bigger dinner table\n")

print(f"Hello Mr. {guests[0].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hi {guests[1].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hello {guests[2].title()} \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come")
print(f"Hello Mr. {guests[3].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hi {guests[4].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hello {guests[5].title()} \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come")
print("Number of guests: ", len(guests))

# Exercise 3.7
guests = ['bill gates', 'marck zuckerberg', 'jeff bezos']
print(f"The Mr. {guests[2].title()} can't come\n")
guests[2] = 'steve jobs'
guests.insert(0, 'steve wozniak')
guests.insert(4, 'alan turing')
guests.append('elon musk')

print("Sorry guys, I can invite only two people for dinner\n")

first_guest = guests.pop(5)
print(f"Sorry Mr. {first_guest.title()} I can invite only two people")

second_guest = guests.pop(4)
print(f"Sorry Mr. {second_guest.title()} I can invite only two people")

third_guest = guests.pop(3)
print(f"Sorry Mr. {third_guest.title()} I can invite only two people")

fourth_guest = guests.pop(0)
print(f"Sorry Mr. {fourth_guest.title()} I can invite only two people")

print(f"Hello {guests[0].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")
print(f"Hi {guests[1].title()} \nI have a dinner in my house the next week, \nI would like you to come\n")

del guests[1]
del guests[0]
print(guests)
print("Number of guests: ", len(guests))