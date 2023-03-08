"""
3.9 Invitado a la Cena

Trabajando con uno de los programas de los Ejercicios 3-4
a 3-7 (página 46), use len() para imprimir un mensaje que 
indique la cantidad de personas que está invitando a cenar
"""

# Exercise 3.4
invitados = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']

mensaje_1 = "Hola Sr." + invitados[0] + " \nTengo una cena la proxima semana, \nMe gustaria que viniera\n"
mensaje_2 = "Hola " + invitados[1] + " \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera\n"
mensaje_3 = "Hola "  + invitados[2] + " \n¿Como esta? \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera"

print(mensaje_1)
print(mensaje_2)
print(mensaje_3)
print("Numero de invitados: ", len(invitados))

# Exercise 3.5
print("El Sr. Jeff Bezos no puede asistir")
invitados = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']
invitados[2] = 'Steve Jobs'

mensaje_1 = "Hola Sr." + invitados[0] + " \nTengo una cena la proxima semana, \nMe gustaria que viniera\n"
mensaje_2 = "Hola " + invitados[1] + " \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera\n"
mensaje_3 = "Hola "  + invitados[2] + " \n¿Como esta? \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera"

print(mensaje_1)
print(mensaje_2)
print(mensaje_3)
print("Numero de invitados: ", len(invitados))

# Exercise 3.6
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
print("Numero de invitados: ", len(invitados))

# Exercise 3.7
print("El Sr. Jeff Bezos no puede venir")
invitados = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']
invitados[2] = 'Steve Jobs'
invitados.insert(0, 'Steve Wozniak')
invitados.insert(4, 'Alan Turing')
invitados.append('Elon Musk')

print("Hola caballeros, Encontre una mesa mas grande ")
print("Lo siento caballeros, Solo puedo invitar a dos personas a cenar\n")

primer_invitado = invitados.pop(5)
print('Lo siento Sr. ' + primer_invitado.title() + ' Solo puedo invitar a dos personas a cenar')
segundo_invitado = invitados.pop(4)
print('Lo siento Sr. ' + segundo_invitado.title() + ' Solo puedo invitar a dos personas a cenar')
tercer_invitado = invitados.pop(3)
print('Lo siento Sr. ' + tercer_invitado.title() + ' Solo puedo invitar a dos personas a cenar')
cuarto_invitado = invitados.pop(0)
print('Lo siento Sr. ' + cuarto_invitado.title() + ' Solo puedo invitar a dos personas a cenar')
print("Numero de invitados: ", len(invitados))

mensaje_1 = "Hola Sr." + invitados[0] + " \nTengo una cena la proxima semana, \nMe gustaria que viniera\n"
mensaje_2 = "Hola " + invitados[1] + " \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera\n"

print(mensaje_1)
print(mensaje_2)
print("Numero de invitados: ", len(invitados))

del invitados[1]
del invitados[0]
print(invitados)
print("Numero de invitados: ", len(invitados))