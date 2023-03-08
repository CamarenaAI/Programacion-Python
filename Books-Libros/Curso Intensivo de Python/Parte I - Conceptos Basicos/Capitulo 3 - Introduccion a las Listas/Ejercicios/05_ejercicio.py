"""
3.5 Cambiar la lista de Invitados

Acabas de escuchar que uno de tus invitados no puede asistir cena, 
por lo que debe enviar un nuevo conjunto de invitaciones. 
Tendrás que pensar en otra persona a quien invitar.
•   Comience con su programa del Ejercicio 3-4. Agregue una declaración impresa al final 
    de su programa que indique el nombre del invitado que no puede asistir.
•   Modifique su lista, reemplazando el nombre del invitado que no puede asistir
    con el nombre de la nueva persona que está invitando.
•   Imprima un segundo conjunto de mensajes de invitación, uno para cada persona 
    que todavía está en su lista.
"""
print("El Sr. Jeff Bezos no puede asistir")
invitados = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']
invitados[2] = 'Steve Jobs'

mensaje_1 = "Hola Sr." + invitados[0] + " \nTengo una cena la proxima semana, \nMe gustaria que viniera\n"
mensaje_2 = "Hola " + invitados[1] + " \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera\n"
mensaje_3 = "Hola "  + invitados[2] + " \n¿Como esta? \nTengo una cena en mi casa la proxima semana, \nMe gustaria que viniera"

print(mensaje_1)
print(mensaje_2)
print(mensaje_3)