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