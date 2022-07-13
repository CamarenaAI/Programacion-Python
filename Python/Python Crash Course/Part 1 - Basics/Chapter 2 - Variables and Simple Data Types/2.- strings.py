# Strings

# Changing Case in a String with Methods
name = "ada lovelace"
print(name.title()) # the method title() converts the first few letters of words to uppercase

name = "ada lovelace"
print(name.upper()) # The method upper() converts all letters in uppercase

name = "ada lovelace"
print(name.lower()) # The method lower() converts all letters in lowercase

# Combinig on Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# Adding Withespace to Strings with Tab or Newlines
print("Python")
print("\tPython") # to add a tab to your text, use the character combination \t
print("Languages:\nPython\nC\nJavaScript")  # to add a new line in a strinf, use the character combination \n
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Withespace
favorite_language = 'python '
print(favorite_language)
favorite_language = ' python '
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)

# Avoiding Syntax Errors with Strings
"""
message = 'One of Python's strengths is its diverse comunity'
print(message)
Output: SyntaxError: invalid syntax
"""
message = "One of Python's strengths is its diverse comunity"
print(message)
