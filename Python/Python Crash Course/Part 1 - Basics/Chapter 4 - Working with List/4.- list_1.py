# Looping Through an Entire List

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician)

# A Closer Look at Looping
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician)

"""
Examples

for cat in cats:
for dog in dogs:
for item in list_of_items:
"""

# Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
 print(magician.title() + ", that was a great trick!") 
 print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Doing Something After a for Loop
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
 print(magician.title() + ", that was a great trick!") 
 print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")
