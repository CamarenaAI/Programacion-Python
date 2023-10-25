from city_functions import city_country

def test_city_country():
    city_country_name = city_country('santiago', 'chile')
    assert city_country_name == 'Santiago, Chile'

def test_city_country_population():
    city_country_name = city_country(
        'santiago', 'chile', '5000000')
    assert city_country_name == "Santiago, Chile - Population 5000000"