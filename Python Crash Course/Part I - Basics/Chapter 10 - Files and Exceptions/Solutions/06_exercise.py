print("Give me two numbers, and I'll add them.")

first_number = input("\nFirst number: ")
second_number = input("Second number: ")

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