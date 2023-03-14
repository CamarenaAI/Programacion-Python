"""
5.10 Comprobación de Nombres de Usuario

Haga lo siguiente para crear un programa que simule cómo los sitios web
aseguran que todos tengan un nombre de usuario único

•   Haz una lista de cinco o más nombres de usuario llamados
    current_users
•   Haga otra lista de cinco nombres de usuario llamada new_users.
    Asegúrese de que uno o dos de los nuevos nombres de usuario también
    estén en la lista current_user
•   Recorra la lista new_users para ver si ya se ha utilizado cada nuevo
    nombre de usuario. Si es así, imprima un mensaje que indique que la
    persona deberá ingresar un nuevo nombre de usuario. Si no se ha
    utilizado un nombre de usuario, imprima un mensaje que diga que el
    nombre de usuario está disponible
•   Asegúrese de que su comparación no distinga entre mayúsculas y
    minúsculas. Si se ha utilizado 'Jhon', no se debe aceptar 'JHON'
"""

current_users = ['Adan', 'Eric', 'Jhon', 'Matt', 'Kevin']
new_users = ['AdAn', 'Tony', 'JHON', 'Charlie', 'Lucas']

for new_user in new_users:
    if new_user.title() in current_users:
        print("Please need to enter a new username")
    else:
        print("The username is available")