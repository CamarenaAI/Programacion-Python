"""
4.5 Sumando un Millon

Haz una lista de los números del uno al millón y luego usa min() y max()
para asegurarte de que tu lista realmente comience en uno y termine en un
millón. Además, use la función sum() para ver qué tan rápido Python puede
agregar un millón de números.
"""

numbers = []
for value in range(1,1000001):
    numbers.append(value)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(numbers)