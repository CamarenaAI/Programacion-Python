"""
3.8 Viendo el Mundo

Piensa en al menos cinco lugares del mundo que te gustaría visitar
•   Almacene las ubicaciones en una lista. Asegúrese de que la lista no
    esté en orden alfabético
•	Imprima su lista en su orden original. No se preocupe por imprimir
    la lista ordenadamente, simplemente imprímala como una lista de 
    Python sin formato

•	Use sorted() para imprimir su lista en orden alfabético sin modificar
    la lista real
•	Muestre que su lista todavía está en su orden original imprimiéndola
•	Use sorted() para imprimir su lista en orden alfabético inverso sin
    cambiar el orden de la lista original
•	Muestre que su lista todavía está en su orden original imprimiéndola
    de nuevo
•	Use reverse() para cambiar el orden de su lista. Imprima la lista
    para mostrar que su orden ha cambiado
•	Use reverse() para cambiar el orden de su lista nuevamente. Imprima
    la lista para mostrar que ha vuelto a su orden original
•	Use sort() para cambiar su lista para que se almacene en orden
    alfabético. Imprima la lista para mostrar que su orden ha sido
    cambiado
•	Use sort() para cambiar su lista para que se almacene en orden
    alfabético inverso. Imprima la lista para mostrar que su orden ha
    cambiado.
"""

places = ['Paris', 'London', 'Rome', 'New York', 'Tokio']

print(places)
print(sorted(places)) # Orden alfabetico
print(sorted(places, reverse=True)) # # Orden alfabetico inverso
places.reverse() # Cambiar el orden de la lista
print(places)
places.reverse() # Cambiar otra vez el orden de la lista
print(places)
places.sort() # Orden alfabetico
print(places)
places.sort(reverse=True) # # Orden alfabetico inverso
print(places)