"""
Que es una Lista?

Una lista es una colección de elementos en un orden particular. Puedes hacer una lista que
incluye las letras del alfabeto, los dígitos del 0 al 9 o los nombres de
todas las personas de tu familia
"""

bicicletas = ['trek', 'cannondale', 'redline', 'specializaed']
print(bicicletas)

# Acceso a elementos de una lista
bicicletas = ['trek', 'cannondale', 'redline', 'specializaed']
print(bicicletas[0])
print(bicicletas[0].title())

# Las posiciones de índice comienzan en 0, no en 1
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas[1])
print(bicicletas[3])
print(bicicletas[-1]) # Al solicitar el elemento en el índice -1, Python siempre devuelve el último elemento de la lista

# Usando valores individuales de una lista
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
mensaje = "Mi primer bicicleta fue una " + bicicletas[0].title() + "."
print(mensaje)
