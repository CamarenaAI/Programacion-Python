languages = ['English', 'Portuguese', 'French', 'German', 'Chinese']
languages[4] = 'Dutch'
languages.append('Spanish')
languages.insert(4, 'Greek')
del languages[4]
languages.pop(3)
languages.remove('French')

print("I speak ", languages[0])
# print("I would like learn ", languages[6]) Error
print(languages)

# Alphabetic order
print(sorted(languages))

# Reverse alphabetic order
print(sorted(languages, reverse=True))

# Change order of your list
languages.reverse()
print(languages)

# Change order of your list again
languages.reverse()
print(languages)

# Alphabetic order
languages.sort()
print(languages)

# Reverse alphabetic order
languages.sort(reverse=True)
print(languages)
print("Number of languages, I would like learn: ", len(languages))