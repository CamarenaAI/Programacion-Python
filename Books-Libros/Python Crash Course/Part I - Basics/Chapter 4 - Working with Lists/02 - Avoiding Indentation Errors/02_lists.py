# Indenting Unnecessarily

"""
message = "Hello Python world!"
    print(message)

 File "hello_world.py", line 2
 print(message)
 ^
IndentationError: unexpected indent
"""

# Indenting Unnecessarily After the loop
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n") 
 
    print("Thank you everyone, that was a great magic show!")