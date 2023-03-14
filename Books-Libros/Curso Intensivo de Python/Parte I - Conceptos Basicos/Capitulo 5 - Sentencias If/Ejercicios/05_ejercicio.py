"""
5.5 Colores alienígenas #3

Convierta su cadena if-else del Ejercicio 5.4 en una cadena if-elif-else

•   Si el color del alienígena es verde, imprime un mensaje de que el
    jugador ganó 5 puntos
•   Si el color del alienígena es amarillo, imprime un mensaje de que el
    jugador ganó 10 puntos
•   Si el color del alienígena es rojo, imprime un mensaje de que el
    jugador ganó 15 puntos
•   Escriba tres versiones de este programa, asegurándose de que cada
    mensaje está impreso para el alienígena de color apropiado
"""

alien_color = 'green'
if alien_color == 'green':
    print("Congratulations, You earn 5 points")
elif alien_color == 'yellow':
    print("Congratulations, You earn 10 points")
elif alien_color == 'red':
    print("Congratulations, You earn 15 points")
else:
    print("Sorry, You don't earn points")