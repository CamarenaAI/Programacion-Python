"""
5.9 Sin Usuarios

Agregue una prueba if a hello_admin.py para asegurarse de que la lista
de usuarios no esté vacía

•   Si la lista está vacía, imprima el mensaje ¡Necesitamos encontrar
    algunos usuarios!
•   Elimine todos los nombres de usuario de su lista y asegúrese de que
    se imprima el mensaje correcto
"""

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Welcome " + username + ", would you like to see status report?")
        else:
            print("Welcome " + username + " thank you for loggin again")
else:
    print("We need to find some user!")