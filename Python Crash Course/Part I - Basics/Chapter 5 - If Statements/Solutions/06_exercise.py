age = 24

if age < 2:
    age = "baby"
elif age >= 2 and age < 4:
    age = "toodler"
elif age >= 4 and age < 13:
    age = "kid"
elif age >= 13 and age < 20:
    age = "teenager"
elif age >= 20 and age < 65:
    age = "adult"
else:
    age = "elder"
    
print(f"The person is a/an {age}")