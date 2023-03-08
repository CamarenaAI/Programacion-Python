"""
5.4 Alien Colors #2

Choose a color for an alien as you did in Exercise 5.3, and
write an if-else chain

•   If the alien's color is green, print a statement that the player just earned
    5 points for shooting the alien
•   If the alien's color isn't green, print a statement that the player just earned
    10 points
•   Write one version of this program that the runs the if block and another that
    runs the else block
"""
# Alien Colors 5.4.1
alien_color = 'green'
if alien_color == 'green':
    print("Congratulations, You earn 5 points")
if alien_color != 'green':
    print("Congratulations, You earn 10 points")

# Alien Colors 5.4.2
alien_color = 'green'
if alien_color == 'green':
    print("Congratulations, You earn 5 points")
else:
    print("Congratulations, You earn 10 points")
