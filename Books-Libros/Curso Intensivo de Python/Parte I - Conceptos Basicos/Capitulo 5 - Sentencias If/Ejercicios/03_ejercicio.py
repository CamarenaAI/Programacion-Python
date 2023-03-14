"""
5.3 Colores Alienígenas #1

Imagina que un extraterrestre acaba de ser derribado en un juego. Cree
una variable llamada alien_color y asígnele un valor de 'verde',
'amarillo' o 'rojo'

•   Escribe un enunciado if para probar si el color del extraterrestre
    es verde. Si es así, imprima un mensaje de que el jugador acaba de
    ganar 5 puntos
•   Escriba una versión de este programa que pase la prueba if y otra
    que falle. (La versión que falla no tendrá salida)
"""

# Colores Alienigenas 5.3.1
alien_color = ['green', 'yellow', 'red'] # Asignarle un valor de 'green', 'yellow', o 'red'
if 'green' in alien_color:               # Asignarle un valor de 'green', 'yellow', o 'red'
    print("Congratulations, You earn 5 points")

# Colores Alienigenas 5.3.2
alien_color = ['white']                  # Asignarle un valor distinto de 'green', 'yellow', o 'red'
if 'green' not in alien_color:           # Asignarle un valor de 'green', 'yellow', o 'red'
    print("Sorry, You don't earn points")