# Tuplas

# Definición de una Tupla
"""
Una tupla se parece a una lista, excepto que usa paréntesis en lugar de
corchetes. Una vez que define una tupla, puede acceder a elementos
individuales utilizando el índice de cada elemento, tal como lo haría
con una lista
"""
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

"""
dimensions = (200, 50)
dimensions[0] = 250

Traceback (most recent call last):
 File "dimensions.py", line 3, in <module>
 dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment
"""

# Recorriendo Todos los Valores en una Tupla
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension,"\n")

# Escribiendo Sobre una Tupla
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
 
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)