def buil_profile(first, last, **user_info):
    """Build a dictionary containing everything we know a bout a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = buil_profile(
    'alonso', 'camarena', location='mexico', 
    field='engineering', programming_language='python')

print(user_profile)