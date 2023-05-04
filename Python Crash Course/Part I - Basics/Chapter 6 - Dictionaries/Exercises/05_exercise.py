rivers = {
    'nile': 'egypt',
    'amazon': 'brasil',
    'mississippi': 'united states of america',
}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())