usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Welcome {username}, would you like to see status report?")
        else:
            print(f"Welcome {username} thank you for loggin again")
else:
    print("We need to find some user!")