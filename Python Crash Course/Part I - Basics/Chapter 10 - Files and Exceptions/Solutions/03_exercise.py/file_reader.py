from pathlib import Path

path = Path('../Files/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)

for line in contents.splitlines():
    print(line)