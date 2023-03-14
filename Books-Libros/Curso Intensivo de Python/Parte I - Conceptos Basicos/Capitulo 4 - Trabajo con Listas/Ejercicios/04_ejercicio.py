"""
4.4 Un Millón

Haz una lista de los números del uno al millón y luego usa un ciclo for
para imprimir los números. (Si la salida tarda demasiado, deténgala
presionando ctrl-C o cerrando la ventana de salida).
"""

numbers = []
for value in range(1, 1000001):
    numbers.append(value)
print(numbers)