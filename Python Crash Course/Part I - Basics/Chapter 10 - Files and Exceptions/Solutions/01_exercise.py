from pathlib import Path

print("- Reading in the entire file -")
path = Path("./Files/learning_python.txt")
contents = path.read_text()
print(contents)

print("\n- Storing the lines in a list and then looping over each line -")
lines = contents.splitlines()
for line in lines:
    print(line)