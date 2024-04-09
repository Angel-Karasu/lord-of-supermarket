from .supermarkets import SuperMarket, Product

COOKIES = {'datadome': 'y3wBsQjboarO8qlMEYZ62GeCJ_oG_m0lohMRkWpgkmfaVssb5d~~sPaYm4H8zUP4tYqIwlHXIwWbtyyohfvUG0Ml1XZVgWDTrUVCFSvNUJsMN8tBf3Szckk40emoQqRZ'}
HEADERS = {'x-red-device': 'red_fo_desktop', 'x-red-version': '3'}

class InterMarche(SuperMarket):
    def __init__(self, cookies:dict[str:str] = {}) -> None: super().__init__('a', 'a', cookies)

    def search(self, searched: str = '', page: int = 1, sort:str = 'pertinence', order:str = 'croissant') -> list[Product]:
        soup = super().search(
            'https://www.intermarche.com/recherche/{searched}?page={page}&trier={sort}&ordre={order}', searched, page,
            'prix' if sort == 'price_absolute' else 'prixkg' if sort == 'price_relative' else 'pertinence',
            'decroissant' if order == 'descendant' else 'croissant'
        )

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