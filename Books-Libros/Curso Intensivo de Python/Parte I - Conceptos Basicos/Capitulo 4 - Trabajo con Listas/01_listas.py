# Ciclo a Través de una Lista Completa

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician)

# Una Mirada más Cercana al Ciclo
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician)

"""
Ejemplos

for cat in cats:
for dog in dogs:
for item in list_of_items:
"""

# Hacer más Trabajo Dentro de un Ciclo for
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(magician.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Hacer Algo Después de un Ciclo for
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")