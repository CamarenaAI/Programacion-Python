"""
5.4 Colores Alienigenas #2

Elija un color para un extraterrestre como lo hizo en el Ejercicio 5.3 y
escriba una cadena if-else

•   Si el color del alienígena es verde, imprime una declaración de que
    el jugador acaba de ganar 5 puntos por dispararle al alienígena.
•   Si el color del alienígena no es verde, imprime una declaración de
    que el jugador acaba de ganar 10 puntos
•   Escriba una versión de este programa que ejecute el bloque if y otra
    que ejecute el bloque else.
"""

# Colores Alienigenas 5.4.1
alien_color = 'green'
if alien_color == 'green':
    print("Congratulations, You earn 5 points")
if alien_color != 'green':
    print("Congratulations, You earn 10 points")

# Colores Alienigenas 5.4.2
alien_color = 'green'
if alien_color == 'green':
    print("Congratulations, You earn 5 points")
else:
    print("Congratulations, You earn 10 points")