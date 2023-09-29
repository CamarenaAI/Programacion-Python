from pathlib import Path

def cats_dogs(path):
    print(f"Reading {filename}:")
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"    Sorry, the file {path} does not exist.\n")
    else:
        print(f"{contents}\n")

filenames = ['./Files/cats.txt',
            './Files/dogs.txt',
            'cats.txt',
            'dogs.txt']

for filename in filenames:
    path = Path(filename)
    cats_dogs(path)