from bs4 import BeautifulSoup
from requests import Session
from typing import Callable

session = Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0'
    
class Product:
    def __init__(self, brand:str, description:str, image_url:str, price_absolute:float, price_relative:float, price_unit:str, quantity_unit:str) -> None:
        self.brand = brand
        self.description = description
        self.image_url = image_url
        self.price_absolute = price_absolute
        self.price_relative = price_relative
        self.price_unit = price_unit
        self.quantity_unit = quantity_unit

class SuperMarket:
    def __init__(self, name:str, address:str, cookies:dict[str, str]) -> None:
        self.name = name
        self.address = address

        self.cookies = cookies

    def search(self, search_url:str, searched, page:int, sort:str, order:str) -> BeautifulSoup:
        return request(search_url.format(searched=searched, page=page, sort=sort, order=order), session.headers, self.cookies)
    
class SuperMarkets:
    def __init__(self, brand:str) -> None:
        self.brand = brand

        self.supermarkets:list[SuperMarket] = []

    def get_supermarkets(self, **kwargs) -> list[SuperMarket]: return []

    def change_function_get_supermarkets(self, func:Callable[[BeautifulSoup], list[SuperMarket]], url:str, headers:dict[str, str], cookies:dict[str, str]):
        self.get_supermarkets = lambda **kwargs: func(request(url.format(kwargs), headers, cookies))
    
    def append_supermarket(self, supermarket:SuperMarket) -> None:
        self.supermarkets.append(supermarket)

    def remove_supermarket(self, supermarket:SuperMarket) -> None:
        self.supermarkets.remove(supermarket)
    

def request(url:str, headers:dict[str, str], cookies:dict[str, str]) -> BeautifulSoup:
    response = session.get(url, headers=headers, cookies=cookies)
    assert response.ok

    return BeautifulSoup(response.content, 'lxml')