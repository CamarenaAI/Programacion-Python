"""
5.9 No Users

Add an if test to hello_admin.py to make sure the list of users is
not empty

•    If the list is empty, print the message We need to find some users!
•    Remove all of usernames from your list, and make sure the correct
message printed
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
