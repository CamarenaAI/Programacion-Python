"""
6.11 Cities

Make a dictionary called cities. Use the names of three cities as keys
in your dictionary. Create a dictionary of information about each city
and include the country that the city is in, its approximate population,
and one fact about that city. The keys for each city’s dictionary should
be something like country, population, and fact. Print the name of each
city and all of the information you have stored about it
"""

cities = {
    'tokyo': {
        'country': 'japan',
        'population': 13.96,
        'fact': 'Tokyo was called Edo for a very long time',
        },
    
    'london': {
        'country': 'England',
        'population': 8.982,
        'fact': 'London is the smallest city in England',
        },
    
    'paris': {
        'country': 'france',
        'population': 2.161,
        'fact': 'Paris was originally a Roman City called “Lutetia”',
        },
    }

for name, city_info in cities.items():
    print("\nCity: " + name.title())
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print("\tCountry: " + country.title())
    print("\tPopulation: " + str(population) + " million")
    print("\tFact: " + fact)