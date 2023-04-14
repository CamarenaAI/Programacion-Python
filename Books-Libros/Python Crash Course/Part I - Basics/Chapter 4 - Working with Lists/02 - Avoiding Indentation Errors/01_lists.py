# Forgetting to Indent

"""
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
print(magician)

 File "magicians.py", line 3 
 print(magician) 
     ^ 
IndentationError: expected an indented block
"""

# Forgetting to Indent Additional Lines
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")