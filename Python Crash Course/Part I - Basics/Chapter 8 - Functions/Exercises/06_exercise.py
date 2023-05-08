def city_country(name, country):
    string_formatted = name + ', ' + country + "\n"
    return string_formatted.title()

city = city_country('santiago', 'chile')
print(city)

city = city_country('guadalajara', 'mexico')
print(city)

city = city_country('las vegas', 'usa')
print(city)