"""
5.10 Checking Usernames

Do the following to create a program that simulates how websites ensure
that everyone has a unique username
•   Make a list of five or more usernames called current_users
•   Make a another list of five usernames called new_users. Make sure
    one or two of the new usernames are also in the current_user list
•   Loop throught the new_users list to see if each a new username has
    alredy been used. If it has, print a message that the person will
    need to enter a new username. If a username has not been used, print
    a message saying that the username is available
•   Make sure your comparison is case insensitive. If 'Jhon' has been
    used, 'JHON' should not be accepted
"""

current_users = ['Adan', 'Eric', 'Jhon', 'Matt', 'Kevin']
new_users = ['AdAn', 'Tony', 'JHON', 'Charlie', 'Lucas']

for new_user in new_users:
    if new_user.title() in current_users:
        print("Please need to enter a new username")
    else:
        print("The username is available")