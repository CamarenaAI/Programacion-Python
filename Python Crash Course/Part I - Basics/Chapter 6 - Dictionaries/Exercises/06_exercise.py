favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

people = ['jen', 'sarah', 'edward', 'phil', 'michael', 'drake', 'axel']
for name in people:
    if name in favorite_languages.keys():
        print("Hi " + name.title() + ", thank you for taking the poll.")
    else:
        print("Hi " + name.title() + ", take a poll please")