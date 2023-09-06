from pathlib import Path

print("Reading in the entire file")
path = Path("./Files/learning_python.txt")
contents = path.read_text()
print(contents)

print("\nReplace the word Python with the name of another language")
lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)

for line in lines:
    line = line.replace('Python', 'Javascript')
    print(line)