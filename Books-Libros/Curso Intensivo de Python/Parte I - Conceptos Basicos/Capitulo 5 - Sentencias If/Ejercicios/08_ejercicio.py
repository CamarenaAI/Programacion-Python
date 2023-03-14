"""
5.8 Hola Admin

Haga una lista de cinco o más nombres de usuario, incluido el nombre
'admin'. Imagine que está escribiendo un código que imprimirá un saludo
para cada usuario después de que inicie sesión en un sitio web. Recorra
la lista e imprima un saludo para cada usuario:

•   Si el nombre de usuario es 'admin', imprima un saludo especial como
    Hola admin, ¿le gustaría ver el informe de estado?
•   De lo contrario, imprima un saludo genérico, como Hola Eric, gracias
    por iniciar sesión nuevamente
"""

usernames = ['admin', 'Eric', 'Jhon', 'Matt', 'Kevin', 
            'Alex', 'Tony', 'Joe', 'Charlie', 'Lucas']

for username in usernames:
    if username == 'admin':
        print("Hello " + username + ", would you like to see status report?")
    else:
        print("Hello " + username + " thank you for loggin again")