"""
4.1 Pizzas

Piensa en al menos tres tipos de tu pizza favorita. Guarde estos nombres
de pizza en una lista y luego use un ciclo for para imprimir el nombre
de cada pizza
•   Modifique su ciclo for para imprimir una oración usando el nombre de
    la pizza en lugar de imprimir solo el nombre de la pizza. Para cada
    pizza, debe tener una línea de salida que contenga una declaración
    simple como Me gusta la pizza de pepperoni
•   Agregue una línea al final de su programa, fuera del bucle for, que
    indique cuánto le gusta la pizza. El resultado debe constar de tres
    o más líneas sobre los tipos de pizza que te gustan y luego una
    oración adicional, como ¡Me encanta la pizza!
"""

pizzas = ['Hawaiian', 'Buffalo', 'Pepperoni']
for pizza in pizzas:
    print("I like " + pizza + " pizza\n" )
print("I really love " + pizzas[0] +  " pizza")
print(pizzas[1] + " pizza is delicious")
print(pizzas[2] + " pizza is the best pizza in the world")