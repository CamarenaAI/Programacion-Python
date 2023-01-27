"""
5.8 Hello Admin

Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a gretting to each user
after they log in to a website. Loop through the list, and print a gretting to
each user:

•    If the username is 'admin', print a special greeting such as Hello admin,
would you like to see status report?
•    Otherwise, print a generic greeting, such as Hello Eric, thank you for 
loggin in again
"""

usernames = ['admin', 'Eric', 'Jhon', 'Matt', 'Kevin', 
            'Alex', 'Tony', 'Joe', 'Charlie', 'Lucas']

for username in usernames:
    if username == 'admin':
        print("Hello " + username + ", would you like to see status report?")
    else:
        print("Hello " + username + " thank you for loggin again")
