"""
3.7 Lista de Invitados cada vez más pequeña

Acaba de enterarse de que su nueva mesa no llegará a tiempo para la cena 
y solo tiene espacio para dos invitados.
•	Comience con su programa del Ejercicio 3-6. Agregue una nueva línea
    que imprima un mensaje que diga que solo puede invitar a dos personas
    a cenar
•	Use pop() para eliminar invitados de su lista uno a la vez hasta que
    solo queden dos nombres en su lista. Cada vez que seleccione un 
    nombre de su lista, imprima un mensaje para esa persona haciéndole 
    saber que lamenta no poder invitarla a cenar.
•	Imprima un mensaje para cada una de las dos personas que todavía están
    en su lista, haciéndoles saber que todavía están invitados.
•	Use del para eliminar los dos últimos nombres de su lista, de modo que
    tenga una lista vacía. Imprima su lista para asegurarse de que
    realmente tiene una lista vacía al final de su programa
"""

print("The Mr. Jeff Bezos can't come")
guests = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']
guests[2] = 'Steve Jobs'
guests.insert(0, 'Steve Wozniak')
guests.insert(4, 'Alan Turing')
guests.append('Elon Musk')

print("Hello guys, I found a bigger dinner table\n")

print("Sorry guys, I can invite only two people for dinner\n")
first_guest = guests.pop(5)
print('Sorry Mr. ' + first_guest.title() + ' I can invite only two people')
second_guest = guests.pop(4)
print('Sorry Mr. ' + second_guest.title() + ' I can invite only two people')
third_guest = guests.pop(3)
print('Sorry Mr. ' + third_guest.title() + ' I can invite only two people')
fourth_guest = guests.pop(0)
print('Sorry Mr. ' + fourth_guest.title() + ' I can invite only two people\n')

message_1 = "Hello " + guests[0] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1] + " \nI have a dinner in my house the next week, \nI would like you to come\n"

print(message_1)
print(message_2)

del guests[1]
del guests[0]
print(guests)