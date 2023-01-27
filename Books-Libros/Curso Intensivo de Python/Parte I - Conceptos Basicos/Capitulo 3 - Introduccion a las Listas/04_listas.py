# Evitar errores de índice al trabajar con listas
"""
motocicletas = ['honda', 'yamaha', 'suzuki'] 
print(motocicletas[3])

Este es un ejemplo da como resultado un error de index:
Traceback (most recent call last):
 File "motorcicletas.py", line 3, in <module>
 print(motorcicletas[3])
IndexError: list index out of range 
"""

motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas[-1])

"""
motocicletas = [] 
print(motocicletas[-1])

No hay elementos en las motocicletas, por lo que Python devuelve otro error de index:
Traceback (most recent call last): 
 File "motocicletas.py", line 3, in <module> 
 print(motocicletas[-1]) 
IndexError: list index out of range
"""