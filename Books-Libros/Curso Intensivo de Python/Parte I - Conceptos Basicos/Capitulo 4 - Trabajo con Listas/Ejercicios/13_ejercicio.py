"""
4.13 Buffet

Un restaurante estilo buffet ofrece solo cinco alimentos básicos. Piense
en cinco alimentos simples y guárdelos en una tupla
•   Use un ciclo for para imprimir cada comida que ofrece el restaurante
•	Intente modificar uno de los elementos y asegúrese de que Python
    rechace el cambio
•	El restaurante cambia su menú, reemplazando dos de los artículos con
    alimentos diferentes. Agregue un bloque de código que reescribe la
    tupla y luego use un bucle for para imprimir cada uno de los
    elementos en el menú revisado
"""

print("Original menu:")
menu = ("eggs", "beans", "chilaquiles", "pork meat", "fish")
# menu[0] = "beef flank steak"
for food in menu:
    print(food)

print("\nModified menu:")
menu = ("salmon", "bbq ribs", "chilaquiles", "pork meat", "fish")
for food in menu:
    print(food)