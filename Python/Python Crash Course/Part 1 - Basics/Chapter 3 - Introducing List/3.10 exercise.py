# 3.10 Every Function
languages = ['English', 'Portuguese', 'French', 'German', 'Chinese']
languages[4] = 'Dutch'
languages.append('Spanish')
languages.insert(4, 'Greek')
del languages[4]
languages.pop(3)
languages.remove('French')
print("I speak ", languages[0])

print(languages)
print(sorted(languages)) # Alphabetic order
print(sorted(languages, reverse=True)) # Reverse alphabetic order
languages.reverse() # Change order of your list
print(languages)
languages.reverse() # Change order of your list again
print(languages)
languages.sort() # Alphabetic order
print(languages)
languages.sort(reverse=True) # Reverse alphabetic order
print(languages)
print("Number of languages, I would like learn: ", len(languages))