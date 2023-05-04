usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Welcome " + username + ", would you like to see status report?")
        else:
            print("Welcome " + username + " thank you for loggin again")
else:
    print("We need to find some user!")