"""
3.6 Más Invitados

Acabas de encontrar una mesa de comedor más grande, así que ahora hay más
espacio disponible. Piensa en tres invitados más para invitar a cenar.
•   Comience con su programa del Ejercicio 3-4 o del Ejercicio 3-5.
    Agregue una declaración impresa al final de su programa informando a
    las personas que encontró una mesa más grande para cenar
•   Use insert() para agregar un nuevo invitado al comienzo de su lista
•   Use insert() para agregar un nuevo invitado al medio de su lista
•   Use append() para agregar un nuevo invitado al final de su lista
•   Imprima un nuevo conjunto de mensajes de invitación, uno para cada
    persona en su lista
"""

print("The Mr. Jeff Bezos can't come")
guests = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']
guests[2] = 'Steve Jobs'
guests.insert(0, 'Steve Wozniak')
guests.insert(4, 'Alan Turing')
guests.append('Elon Musk')

print("Hello guys, I found a bigger dinner table ")

message_1 = "Hello Mr." + guests[0] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_3 = "Hello "  + guests[2] + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"
message_4 = "Hello Mr." + guests[3] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_5 = "Hi " + guests[4] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_6 = "Hello "  + guests[5] + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"

print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)