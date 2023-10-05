from pathlib import Path
import json

path = Path('./Files/numbers.json')

# Writer
print("Writer")
number = input('Please insert your favorite number: ')
contents = json.dumps(number)
path.write_text(contents)
print(f"I know your favorite number!")

# Reader
print("\nReader")
contents = path.read_text()
numbers = json.loads(contents)
print(f"I know your favorite number! It's {number}")