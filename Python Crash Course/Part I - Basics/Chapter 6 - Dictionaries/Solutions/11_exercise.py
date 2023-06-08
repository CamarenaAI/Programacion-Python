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
    print(f"\nCity: {name.title()}")
    
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population} million")
    print(f"\tFact: {fact}")