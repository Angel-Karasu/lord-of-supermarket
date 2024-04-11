from requests import Session

from .utils.address import Address
from .utils.product import Product

session = Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0'

class SuperMarket:
    def __init__(self, name:str, address:Address, cookies:dict[str, str]) -> None:
        self.name = name
        self.address = address

        self.cookies = cookies

    def search_products(self, search:str, page:int, sort:str, order:str) -> list[Product]: return []
    
class SuperMarkets:
    def __init__(self, brand:str, base_url:str) -> None:
        self.brand = brand
        self.base_url = base_url

        self.supermarkets:list[SuperMarket] = []

    def get_supermarkets_by_postal_code(self, postal_code:int) -> list[SuperMarket]:
        return [market for market in self.supermarkets if str(postal_code) in str(market.address.postal_code)]