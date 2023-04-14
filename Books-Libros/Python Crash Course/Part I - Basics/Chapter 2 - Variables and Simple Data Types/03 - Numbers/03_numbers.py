# Avoiding Type Errors with the str() Function

"""
age = 23
message = "Happy " + age + "rd Birthday"
print(message)
Output: SyntaxError: invalid syntax
"""

age = 23
message = "Happy " + str(age) + "rd Birthday" # You can do this by wrapping the variable in the str() function, which tells Python to represent non-string values as strings
print(message)