from modules.clear import *
from order_details import *
from modules.modules import *

class Order(Modules):
    
    def __init__(self):
        self._username
        self._order = []


    def cart(self, item, amount):
        pass
        


    def _calc_total(self, subtotal, taxes = 0.21):
        return subtotal * (subtotal * taxes)