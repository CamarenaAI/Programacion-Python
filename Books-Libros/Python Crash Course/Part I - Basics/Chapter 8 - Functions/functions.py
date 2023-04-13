# Defining a Function

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# Passing Information to a Function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')

# Arguments and Parameters
"""
Argument: Is a piece of information that is passed from a function
call to a function. Are the variables passed to the function in the
function call

Parameters: Are the variables used in the function definition
"""