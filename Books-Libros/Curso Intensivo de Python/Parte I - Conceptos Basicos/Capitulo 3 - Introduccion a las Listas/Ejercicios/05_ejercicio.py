"""
3.5 Cambiar la lista de Invitados

Acabas de escuchar que uno de tus invitados no puede asistir cena, por 
lo que debe enviar un nuevo conjunto de invitaciones. Tendrás que pensar
en otra persona a quien invitar.
•   Comience con su programa del Ejercicio 3-4. Agregue una declaración
    impresa al final de su programa que indique el nombre del invitado
    que no puede asistir.
•   Modifique su lista, reemplazando el nombre del invitado que no puede
    asistir con el nombre de la nueva persona que está invitando.
•   Imprima un segundo conjunto de mensajes de invitación, uno para cada
    persona que todavía está en su lista.
"""

print("The Mr. Jeff Bezos can't come")
guests = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']
guests[2] = 'Steve Jobs'

message_1 = "Hello Mr." + guests[0] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_3 = "Hello "  + guests[2] + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"

print(message_1)
print(message_2)
print(message_3)