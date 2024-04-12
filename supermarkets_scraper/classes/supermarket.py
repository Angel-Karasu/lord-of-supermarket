from requests import Session

from .address import Address
from .product import Product

session = Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0'

class SuperMarket:
    def __init__(self, name:str, address:Address, base_url:str, cookies:dict[str, str]) -> None:
        self.name = name
        self.address = address
        self.base_url = base_url

        self.cookies = cookies

    def search_products(self, search:str, page:int, sort:str, order:str) -> list[Product]: return []
    
class SuperMarkets:
    def __init__(self, brand:str, base_url:str) -> None:
        self.brand = brand
        self.base_url = base_url

        self.supermarkets:list[SuperMarket] = []

    def get_supermarkets_by_postal_code(self, postal_code:int) -> list[SuperMarket]:
        return [(market, i) for i, market in enumerate(self.supermarkets) if str(postal_code) in str(market.address.postal_code)]
    
    def search_products(self, list_index_supermarket:list[int], search:str, page:int, sort:str, order:str) -> dict[int, list[Product]]:
        return {i: self.supermarkets[i].search_products(search, page, sort, order) for i in list_index_supermarket}