# Evitar Errores de Sangría

# Olvidando las Sangrías
"""
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
print(magician)

 File "magicians.py", line 3 
 print(magician) 
     ^ 
IndentationError: expected an indented block
"""

# Olvidando las Sangrías, Líneas Adicionales
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Sangría Innecesaria
"""
message = "Hello Python world!"
    print(message)

 File "hello_world.py", line 2
 print(message)
 ^
IndentationError: unexpected indent
"""

# Sangría Innecesaria Después del Ciclo
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n") 
 
    print("Thank you everyone, that was a great magic show!")

# Olvidando los Dos Puntos
"""
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians
    print(magician)
"""