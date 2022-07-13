"""
3.10 Every Function

Think of something you could store in a list. For example, 
you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items 
and then uses each function introduced in this chapter at least once
"""
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
