from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user information if available"""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None
    
def get_new_user_info(path):
    """Prompt for new user information."""
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
    stored_user_info = get_stored_user_info(path)
    
    if stored_user_info:
        correct_username = input(f"Is {stored_user_info['username']} your correct username? (yes/no): ").strip().lower()
        
        if correct_username != "yes":
            stored_user_info = get_new_user_info(path)
            print(f"We'll update your username to {stored_user_info['username']}.")

        print(f"Welcome back, {stored_user_info['username']}\n"
            f"ID Number: {stored_user_info['idnumber']}\n"
            f"Current Level Range: {stored_user_info['level']}")

    else:
        stored_user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {stored_user_info['username']}!")

greet_user()