"""
4.10 Slices

Usando uno de los programas que escribió en este capítulo, agregue varias
líneas al final del programa que hagan lo siguiente:
•   Imprima el mensaje. Los primeros tres elementos de la lista son:.
    Luego, use un slice para imprimir los primeros tres elementos de
    la lista de ese programa.
•   Imprima el mensaje. Los tres elementos de la mitad de la lista son:.
    Use un slice para imprimir tres elementos desde el medio de la 
    lista
•   Imprima el mensaje. Los últimos tres elementos de la lista son:.
    Utilice un slice para imprimir los últimos tres elementos de la
    lista
"""

pizzas = ['Hawaiian', 'Buffalo', 'Pepperoni', 'Cheese', 'Veggie', 'Meat', 'BBQ Chicken', 'Supreme', 'Margherita']
for pizza in pizzas:
    print("This is a " + pizza + " pizza\n" )
print(pizzas[0:3])
print(pizzas[3:6])
print(pizzas[6:9])
