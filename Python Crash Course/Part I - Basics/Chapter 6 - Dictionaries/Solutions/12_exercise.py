companies = {
    'meta': {
        'first_name': 'mark',
        'last_name': 'zuckerber',
        'age': 38, 
        'city': 'white plains',
        },

    'amazon': {
        'first_name': 'jeff',
        'last_name': 'bezos',
        'age': 59,
        'city': 'albuquerque',
        },

    'microsoft': {
        'first_name': 'bill',
        'last_name': 'gates',
        'age': 67,
        'city': 'seattle',
        }
    }

for name, company_info in companies.items():
    print(f"\nCompany: {name.title()}")

    full_name = company_info['first_name'] + company_info['last_name']
    city = company_info['city']
    age = company_info['age']
    
    print(f"\tCEO: {full_name.title()} live in {city.title()}" 
        f" and He is {age} years")