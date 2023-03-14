"""
Que es una Lista?

Una lista es una colección de elementos en un orden particular. Puedes
hacer una lista que incluye las letras del alfabeto, los dígitos del 0 al
9 o los nombres de todas las personas de tu familia
"""

bicycles = ['trek', 'cannondale', 'redline', 'specializaed']
print(bicycles)

# Acceso a elementos de una lista
bicycles = ['trek', 'cannondale', 'redline', 'specializaed']
print(bicycles[0])
print(bicycles[0].title())

# Las posiciones de índice comienzan en 0, no en 1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]) # Al solicitar el elemento en el índice -1, Python siempre devuelve el último elemento de la lista

# Usando valores individuales de una lista
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)