"""
6.4 Glossary 2

Now that you know how to loop through a dictionary, clean up the code
from Exercise 6.3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary's keys and
values. When you're sure that your loop works, add five more Python
therms to your glossary. When you run your program again, these new
words and meanings should automatically be included in the output
"""

programming_words = {
    'variable': 'symbolic name that is a reference or pointer to an object',
    'string': 'collection of alphabets, words or other characters',
    'list': 'data structure in Python that is a mutable, or changeable, ordered sequence of elements',
    'tuple': 'store multiple items in a single variable',
    'dictionary': 'Python´s implementation of a data structure that is more generally known as an associative array',
    'float': 'function or reusable code in the Python programming language that converts values into floating point numbers',
    'for': 'a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied',
    'if': ' a conditional statement in python, that is used to determine whether a block of code will be executed or not',
    'else': 'used in conditional statements (if statements), and decides what to do if the condition is False',
    'comments': 'the inclusion of short descriptions along with the code to increase its readability',
}

for word, definition in programming_words.items():
    print(word + ": " + definition)