from json import loads

from .intermarche import HEADERS, COOKIES
from .supermarkets import session

class City:
    def __init__(self, postal_code:int, city:str, country:str, latitude:float, longitude:float) -> None:
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude

def get_city_by_postal_code(postal_code:int) -> City:
    city = loads(session.get(
        f'https://www.intermarche.com/api/service/geolocalisation/v1/addresses/search?input={postal_code}&country=FRA',
        headers=HEADERS,
        cookies=COOKIES
    ).text)[0]

    return City(city['postalCode'], city['city'], city['country'], city['latitude'], city['longitude'])