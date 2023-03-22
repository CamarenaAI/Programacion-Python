"""
6.3 Glossary

A Python dictionary can be used to model an actual dictionary. However,
to avoid confusion, let's call it a glossary
•   Think of five programming words you´ve learned about in the previous
    chapters. Use these words as the keys in your glossary, and store
    their meanings as values
•   Print each word and its meaning as neatly formatted output. You
    might print the word followed by a colon and then its meaning, or
    print the word on one line and then print its meaning intended on a
    second line. Use the newline character (\n) to insert a blank line
    between each word-meaning pair in your output
"""

programming_words = {
    'variable': 'symbolic name that is a reference or pointer to an object',
    'string': 'collection of alphabets, words or other characters',
    'list': 'data structure in Python that is a mutable, or changeable, ordered sequence of elements',
    'tuple': 'store multiple items in a single variable',
    'dictionary': 'Python´s implementation of a data structure that is more generally known as an associative array',
}

print("variable: " + programming_words['variable'] + "\n"
    "string: " + programming_words['string'] + "\n"
    "list: " + programming_words['list'] + "\n"
    "tuple: " + programming_words['tuple'] + "\n"
    "dictionary: " + programming_words['dictionary'] + "\n")