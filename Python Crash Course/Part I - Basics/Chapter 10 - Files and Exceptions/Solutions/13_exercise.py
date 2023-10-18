from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    idnumber = input("What is your ID number? ")
    level = input("What is your current level? (Bronze, Silver, Gold) ")

    user_info = {
        'username': username.lower(),
        'idnumber': idnumber,
        'level': level.title()
    }

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    """Greet the user by name"""
    path = Path('./Files/username.json')
    user_info = get_stored_username(path)
    if user_info:
        print(f"Welcome back, {user_info['username']}\n"
            f"ID Number: {user_info['idnumber']}\n"
            f"Current Level Range: {user_info['level']}")
    else:
        user_info = get_new_username(path)
        print(f"We'll remember you when you come back, {user_info['username']}!")

greet_user()