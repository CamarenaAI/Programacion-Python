# Looping Through All Values in a Dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())