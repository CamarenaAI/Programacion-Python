favorite_places = {
    'george': ['paris', 'vancouver', 'disneyland'],
    'seraphina': ['malibu', 'las vegas'],
    'john': ['hawai', 'vancouver'],
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())