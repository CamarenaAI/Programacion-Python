"""
3.4 Lista de Invitados

Si pudieras invitar a alguien, vivo o fallecido, a cenar, 
¿a quién invitarías? Haz una lista que incluya al menos tres personas a
las que te gustaría invitar a cenar. Luego use su lista para imprimir un
mensaje para cada persona, invitándolos a cenar
"""

guests = ['Bill Gates', 'Marck Zuckerberg', 'Jeff Bezos']

message_1 = "Hello Mr." + guests[0] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_2 = "Hi " + guests[1] + " \nI have a dinner in my house the next week, \nI would like you to come\n"
message_3 = "Hello "  + guests[2] + " \nHow are you? \nI have a dinner in my house the next week, \nI would like you to come"

print(message_1)
print(message_2)
print(message_3)