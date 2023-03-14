"""
5.2 Más pruebas condicionales

No tiene que limitar la cantidad de pruebas que crea a 10. Si desea
probar más comparaciones, escriba más pruebas y agréguelas a 
conditional_tests.py. Tenga al menos un resultado verdadero y uno falso
para cada uno de los siguientes:

•   Pruebas de igualdad y desigualdad con strings
•   Pruebas usando la función lower()
•   Pruebas numéricas que involucran igualdad y desigualdad, mayor que y
    menor que, mayor que o igual a, y menor que o igual a
•   Pruebas usando la palabra clave "and" y la palabra clave "or"
•   Probar si un elemento está en una lista
•   Probar si un elemento no está en una lista
"""

# Pruebas de igualdad y desigualdad con strings
name = 'Alonso'
if name == 'Alonso':
    print('Wellcome back, Alonso')
else:
    print('You are not Alonso')

programming_language = 'java'
if programming_language != 'python':
    print('Python is more easy to learn')
else:
    print('Good choose')

# Pruebas usando la función lower()
country = 'MeXiCo'
if country.lower() == 'mexico':
    print('You are mexican')
else:
    print("Where are you from?")

# Prueba Numerica
age = 18
if age == 18:
    print(True)
else:
    print("You are not 18")

if age != 18:
    print("You are not 18")
else:
    print("You are 18")

# Pruebas usando la palabra clave "and" y la palabra clave "or"
name = 'Andres'
age = 18
if name == 'Gabriel' or age >= 18:
    print("Please come in")
else:
    print("You can't pass")

name = 'Andres'
age = 21
if name == 'Andres' and age >= 21:
    print("Please come in Mr. Andres")
else:
    print("You can't pass")

# Probar si un elemento está en una lista
fruits = ['pinapple', 'apple', 'grape', 'pear']
if 'pinapple' in fruits:
    print(True)

# Probar si un elemento no está en una lista
fruits = ['pinapple', 'apple', 'grape', 'pear']
fruit = 'guava'
if fruit not in fruits:
    print(fruit.title() + " is not in the list")