current_users = ['Adan', 'Eric', 'Jhon', 'Matt', 'Kevin']
new_users = ['AdAn', 'Tony', 'JHON', 'Charlie', 'Lucas']

for new_user in new_users:
    if new_user.title() in current_users:
        print("Please need to enter a new username")
    else:
        print("The username is available")