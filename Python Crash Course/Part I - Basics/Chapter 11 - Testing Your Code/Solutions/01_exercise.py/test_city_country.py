from city_functions import city_country

def test_city_country():
    city_country_name = city_country('santiago', 'chile')
    assert city_country_name == 'Santiago, Chile'