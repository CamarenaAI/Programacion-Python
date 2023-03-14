"""
4.2 Animales
Piensa en al menos tres animales diferentes que tengan una característica
común. Guarde los nombres de estos animales en una lista y luego use un
ciclo for para imprimir el nombre de cada animal
•   Modifique su programa para imprimir una declaración sobre cada
    animal, como Un perro sería una gran mascota
•   Agregue una línea al final de su programa indicando lo que estos
    animales tienen en común. Podría escribir una oración como
    ¡Cualquiera de estos animales sería una gran mascota!
"""

animals = ['dog', 'cat', 'fish']
for animal in animals:
    print(animal)
    print("The " + animal + " is a pet")
print("Any of these animals would make a great pet!")