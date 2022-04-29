from modules.modules import *
from modules.modules import *

class Products:

    def __init__(self):
        self._products_info = {}


    def add_product(self, name, price, stock, supplier):
        self._products_info = {"id": self.last_key(), "name": name, "price": price, "stock": stock, "supplier": supplier, "reviews": {}}
