from pathlib import Path

def silent_cats_dogs(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"Reading {filename}:")
        print(f"{contents}\n")

filenames = ['./Files/cats.txt',
            './Files/dogs.txt',
            'cats.txt',
            'dogs.txt'] 

for filename in filenames:
    path = Path(filename)
    silent_cats_dogs(path)