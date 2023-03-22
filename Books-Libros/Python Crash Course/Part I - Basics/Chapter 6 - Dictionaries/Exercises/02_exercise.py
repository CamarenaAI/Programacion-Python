"""
6.2 Favorite Numbers

Use a dictionary to store people's favorite numbers. Think of five names
and use them as keys in your dictionary. Think of a favorite number for
each person, and store each as a value in your dictionary. Print each
person's name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program
"""

people_numbers = {
    'paul': 1,
    'john': 13,
    'sarah': 26,
    'stephanie': 22,
    'axel': 2,
}

print("Paul favorite number is " + str(people_numbers['paul']) + "\n"
      "John favorite number is " + str(people_numbers['john']) + "\n"
      "Sarah favorite number is " + str(people_numbers['sarah']) + "\n"
      "Stephanie favorite number is " + str(people_numbers['stephanie']) + "\n"
      "Axel favorite number is " + str(people_numbers['axel']))