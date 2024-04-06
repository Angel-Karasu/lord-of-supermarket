from requests import utils, Session
from bs4 import BeautifulSoup

AVAILABLE_METHODS = ['delete', 'get', 'head', 'patch', 'post', 'put']
HEADERS = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0'}

class Market:
    def __init__(self, cookies:dict[str:str]) -> None:
        self.session = Session()
        self.session.cookies = utils.cookiejar_from_dict(cookies)
        self.session.headers = HEADERS

    def search(self, method:str, search_url:str, searched, page:int, sort:str, order:str) -> BeautifulSoup:
        return request(self, method, search_url.format(searched=searched, page=page, sort=sort, order=order))
    
class Product:
    def __init__(self, brand:str, description:str, image_url:str, price_absolute:float, price_relative:float, price_unit:str, quantity_unit:str) -> None:
        self.brand = brand
        self.description = description
        self.image_url = image_url
        self.absolute_price = price_absolute
        self.price_relative = price_relative
        self.price_unit = price_unit
        self.quantity_unit = quantity_unit


def request(market:Market, method:str = 'get', url:str = '') -> BeautifulSoup:
    assert method in AVAILABLE_METHODS, f'Used method `{method}` not in {AVAILABLE_METHODS}'

    response = market.session.request(method, url)
    assert response.ok

    return BeautifulSoup(response.content, 'lxml')