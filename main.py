from supermarkets import intermarche

im_grenoble = intermarche.InterMarche(
    cookies={'itm_pdv':'{%22ref%22:%2210603%22%2C%22name%22:%22Super%2520Grenoble%22%2C%22city%22:%22Grenoble%22}'}
)

products = im_grenoble.search('lait', 1)

print(list(map(lambda product: vars(product), products)))

import urllib.parse

print(({"ref":"10603","isEcommerce":True,"name":"Super%20Grenoble","city":"Grenoble"}))

import requests, json
from bs4 import BeautifulSoup

from supermarkets import supermarkets, city

session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0'

INTERMARCHE = supermarkets.SuperMarkets('Intermarché')

print(session.get(
    'https://www.intermarche.com/api/service/pdvs/v4/pdvs/zone?r=10000&lat=47.3833270209&lon=-1.18241880879&min=10&postalCode=44150',
    headers={'x-red-device': 'red_fo_desktop', 'x-red-version': '3'},
    cookies={'datadome': 'y3wBsQjboarO8qlMEYZ62GeCJ_oG_m0lohMRkWpgkmfaVssb5d~~sPaYm4H8zUP4tYqIwlHXIwWbtyyohfvUG0Ml1XZVgWDTrUVCFSvNUJsMN8tBf3Szckk40emoQqRZ'}
).text)

print(city.get_city_by_postal_code(38000))