class Product:
    def __init__(self, brand:str, description:str, image_url:str, price_absolute:float, price_relative:float, price_unit:str, quantity_unit:str) -> None:
        self.brand = brand
        self.description = description
        self.image_url = image_url
        self.price_absolute = price_absolute
        self.price_relative = price_relative
        self.price_unit = price_unit
        self.quantity_unit = quantity_unit