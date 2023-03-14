"""
4.11 Mis Pizzas, Tus Pizzas

Comience con su programa del Ejercicio 4-1 (página 60). Haga una copia de
la lista de pizzas y llámela friend_pizzas. Luego, haz lo siguiente:
•   Agregar una nueva pizza a la lista original
•   Añadir una pizza diferente a la lista friend_pizzas
•   Demuestra que tienes dos listas separadas. Imprima el mensaje Mis
    pizzas favoritas son: y luego use un ciclo for para imprimir la
    primera lista. Imprima el mensaje, Las pizzas favoritas de mi amigo
    son: y luego use un ciclo for para imprimir la segunda lista.
    Asegúrese de que cada nueva pizza se almacene en la lista adecuada
"""

pizzas = ['Hawaiian', 'Buffalo', 'Pepperoni']
pizzas.append('BBQ Chicken')
print("My favorite pizzas are:\n", pizzas)

friend_pizzas = ['Cheese', 'Veggie', 'Meat']
friend_pizzas.append('Supreme')
print("My friend’s favorite pizzas are:\n", friend_pizzas)