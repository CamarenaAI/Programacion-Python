"""
8.6 City Names

Write a function called city_country() that takes in the name of a
city and its country. The function should return a string formatted
like this:

"Santiago, Chile"

Call your function with at least three city-country pairs, and print 
the value that’s returned.
"""

def city_country(name, country):
    string_formatted = name + ', ' + country + "\n"
    return string_formatted.title()

city = city_country('santiago', 'chile')
print(city)

city = city_country('guadalajara', 'mexico')
print(city)

city = city_country('las vegas', 'usa')
print(city)