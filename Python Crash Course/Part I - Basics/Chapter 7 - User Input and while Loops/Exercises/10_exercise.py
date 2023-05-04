responses = {}

polling_active = True
while polling_active:
    response = input("If you could visit one place in the world, where would you go? ")
    responses[response] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for response in responses.values():
    print(response.title())