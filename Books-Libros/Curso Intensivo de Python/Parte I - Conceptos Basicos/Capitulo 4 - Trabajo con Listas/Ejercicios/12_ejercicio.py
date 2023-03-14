"""
4.12 Mas Ciclos

Todas las versiones de foods.py en esta sección han evitado el uso de
ciclo for al imprimir para ahorrar espacio. Elija una versión de
foods.py y escriba dos bucles for para imprimir cada lista de alimentos
"""

# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for foods in my_foods:
    print("My favorite foods are:")
    print(foods)
for foods in friend_foods:
    print("\nMy friend's favorite foods are:")
    print(foods)
