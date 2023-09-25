from pathlib import Path

path = Path('./Files/guest_book.txt')
guest = []

prompt = "\nWhat is your name?"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    name = input(prompt)
    if name.lower() == 'quit':
        break
    else:
        print(f"You'll add {name.title()} to your guest book!")
        guest.append(name.title())

path.write_text('\n'.join(guest) + '\n')