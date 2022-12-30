"""
5.3 Alien Colors #1

Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'

•    Write an if statement to test whether the alien's color is green. If it is, print
a message that the player just earned 5 points 
•    Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
"""
# Alien Color 5.3.1
alien_color = ['green', 'yellow', 'red'] # Assign it a value of 'green', 'yellow', or 'red'
if 'green' in alien_color:               # Assign it a value of 'green', 'yellow', or 'red'
    print("Congratulations, You earn 5 points")

# Alien Color 5.3.2
alien_color = ['white']                  # Assign it a value distinct of 'green', 'yellow', or 'red'
if 'green' not in alien_color:           # Assign it a value of 'green', 'yellow', or 'red'
    print("Sorry, You don't earn points")
