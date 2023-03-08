"""
3.6 Más Invitados

Acabas de encontrar una mesa de comedor más grande, así que ahora hay más espacio
disponible. Piensa en tres invitados más para invitar a cenar.
•   Comience con su programa del Ejercicio 3-4 o del Ejercicio 3-5. Agregue una declaración 
    impresa al final de su programa informando a las personas que encontró una mesa más grande 
    para cenar
•   Use insert() para agregar un nuevo invitado al comienzo de su lista
•   Use insert() para agregar un nuevo invitado al medio de su lista
•   Use append() para agregar un nuevo invitado al final de su lista
•   Imprima un nuevo conjunto de mensajes de invitación, uno para cada persona en su lista
"""
print("El Sr. Jeff Bezos no puede venir")
invitados = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']
invitados[2] = 'Steve Jobs'
invitados.insert(0, 'Steve Wozniak')
invitados.insert(4, 'Alan Turing')
invitados.append('Elon Musk')

print("Hola caballeros, Encontre una mesa mas grande ")

mensaje_1 = "Hola Sr." + invitados[0] + " \nTengo una cena la proxima semana, \nMe gustaria que viniera\n"
mensaje_2 = "Hola " + invitados[1] + " \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera\n"
mensaje_3 = "Hola "  + invitados[2] + " \n¿Como esta? \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera"
mensaje_4 = "Hello Mr." + invitados[3] + "  \nTengo una cena la proxima semana, \nMe gustaria que viniera\n"
mensaje_5 = "Hi " + invitados[4] + "  \nTengo una cena la proxima semana, \nMe gustaria que viniera\n"
mensaje_6 = "Hello "  + invitados[5] + " \n¿Como esta? \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera"

print(mensaje_1)
print(mensaje_2)
print(mensaje_3)
print(mensaje_4)
print(mensaje_5)
print(mensaje_6)