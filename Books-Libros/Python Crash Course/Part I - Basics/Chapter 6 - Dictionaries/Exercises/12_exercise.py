"""
6.12 Extensions
                                                                       |
We’re now working with examples that are complex enough that they can be
extended in any number of ways. Use one of the example programs from
this chapter, and extend it by adding new keys and values, changing the
context of the program or improving the formatting of the output
"""

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
    print("\nCompany: " + name.title())
    full_name = company_info['first_name'] + company_info['last_name']
    city = company_info['city']
    age = company_info['age']
    print("\tCEO: " + full_name.title() + " live in " + city.title() + 
        " and He is " + str(age) + " years")