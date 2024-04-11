from bs4 import BeautifulSoup
from json import loads

from ..utils.address import Address
from ..utils.product import Product
from ..supermarkets import session, SuperMarket, SuperMarkets

INTERMARCHES = SuperMarkets('Intermarché', 'www.intermarche.com')

class InterMarche(SuperMarket):
    def __init__(self, name: str, address: Address, id:str) -> None:
        super().__init__(
            name, address, {'itm_pdv': str({'ref': id, 'name': f'{name.split()[1]} {address.city}', 'city': address.city}).replace("'", '"')}
        )

    def search_products(self, search:str = '', page:int = 1, sort:str= '', order:str = '') -> list[Product]:
        sort = 'prix' if sort == 'price_absolute' else 'prixkg' if sort == 'price_relative' else 'pertinence',
        order = 'decroissant' if order == 'descendant' else 'croissant'

        res = session.get(
            f'https://{INTERMARCHES.base_url}/recherche/{search}?page={page}&trier={sort}&ordre={order}',
            cookies=self.cookies
        )
        soup = BeautifulSoup(res.content, 'lxml')

        products = []

        for product in soup.select('.stime-product-card-course'):
            try: products.append(Product(
                product.select_one('.stime-product--details__summary > p').text,
                product.select_one('.stime-product--details__title').text,
                product.select_one('.stime-product--details__image')['src'],
                float(product.select_one('.product--price').text.split(' ')[0].replace(',', '.')),
                float(product.select_one('.content-S-R').text.split(' ')[-2].replace(',', '.')),
                '€',
                product.select_one('.content-S-R').text.split('/')[-1],
            ))
            except: pass

        return products

for market in loads(session.get(f'https://{INTERMARCHES.base_url}/api/service/pdvs/v4/pdvs/zone?r=10000',
        headers={'x-red-device': 'red_fo_desktop', 'x-red-version': '3'},
        cookies={'datadome': 'y3wBsQjboarO8qlMEYZ62GeCJ_oG_m0lohMRkWpgkmfaVssb5d~~sPaYm4H8zUP4tYqIwlHXIwWbtyyohfvUG0Ml1XZVgWDTrUVCFSvNUJsMN8tBf3Szckk40emoQqRZ'}
    ).text)['resultats']:

    add = market['addresses'][0]

    INTERMARCHES.supermarkets.append(InterMarche(
        INTERMARCHES.brand + ' ' + market['modelLabel'].title(),
        Address(add['address'], int(add['postCode']), add['townLabel'], **{l:float(add[l]) for l in ['latitude', 'longitude']}),
        market['entityCode']
    ))