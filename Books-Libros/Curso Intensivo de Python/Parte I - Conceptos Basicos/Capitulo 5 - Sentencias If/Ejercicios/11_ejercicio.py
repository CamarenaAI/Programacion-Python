"""
5.11 Números Ordinales

Los números ordinales indican su posición en una lista, como 1º o 2º.
La mayoría de los números ordinales terminan en th, excepto 1, 2 y 3

•   Almacene los números del 1 al 9 en una lista
•   Recorrer la lista
•   Use una cadena if-elif-else dentro del ciclo para imprimir el final
    ordinal apropiado para cada número. Su salida debe leer 1st 2nd 3rd
    4th 5th 6th 7th 8th 9th y cada resultado debe estar en una línea 
    separada
"""

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(str(ordinal_number) + "st")
    elif ordinal_number == 2:
        print(str(ordinal_number) + "nd")
    elif ordinal_number == 3:
        print(str(ordinal_number) + "rd")
    else:
        print(str(ordinal_number) + "th")