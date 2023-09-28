print("Give me two numbers, and I'll add them.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("\nYou can't add: \n" 
            "- number and a character/letter,\n" 
            "- two characters/letters,\n"
            "- float numbers\n"
            "Please try one more time")
    else:
        print(f"{first_number} + {second_number} = {answer}")
        break