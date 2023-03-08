"""
3.7 Lista de Invitados cada vez más pequeña

Acaba de enterarse de que su nueva mesa no llegará a tiempo para la cena 
y solo tiene espacio para dos invitados.
•	Comience con su programa del Ejercicio 3-6. Agregue una nueva línea 
    que imprima un mensaje que diga que solo puede invitar a dos personas a cenar
•	Use pop() para eliminar invitados de su lista uno a la vez hasta que solo queden 
    dos nombres en su lista. Cada vez que seleccione un nombre de su lista, 
    imprima un mensaje para esa persona haciéndole saber que lamenta no poder invitarla a cenar.
•	Imprima un mensaje para cada una de las dos personas que todavía están en su lista, 
    haciéndoles saber que todavía están invitados.
•	Use del para eliminar los dos últimos nombres de su lista, de modo que tenga una lista vacía. 
    Imprima su lista para asegurarse de que realmente tiene una lista vacía al final de su programa
"""
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

mensaje_1 = "Hola Sr." + invitados[0] + " \nTengo una cena la proxima semana, \nMe gustaria que viniera\n"
mensaje_2 = "Hola " + invitados[1] + " \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera\n"

print(mensaje_1)
print(mensaje_2)

del invitados[1]
del invitados[0]
print(invitados)
