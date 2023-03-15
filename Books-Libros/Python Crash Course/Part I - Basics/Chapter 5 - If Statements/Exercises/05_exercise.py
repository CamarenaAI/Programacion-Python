"""
5.5 Alien Colors #3

Turn your if-else chain from Exercise 5.4 into if-elif-else chain 
•   If the alien's color is green, print a message that the player
    earned 5 points
•   If the alien's color is yellow, print a message that the player
    earned 10 points
•   If the alien's color is red, print a message that the player earned
    15 points
•   Write three versions of this program, making sure each message is
    printed for the appropriate color alien
"""

alien_color = 'green'
if alien_color == 'green':
    print("Congratulations, You earn 5 points")
elif alien_color == 'yellow':
    print("Congratulations, You earn 10 points")
elif alien_color == 'red':
    print("Congratulations, You earn 15 points")
else:
    print("Sorry, You don't earn points")