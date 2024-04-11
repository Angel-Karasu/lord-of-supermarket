class Address:
    def __init__(self, address:str, postal_code:int, city:str, latitude:float, longitude:float) -> None:
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.latitude = latitude
        self.longitude = longitude