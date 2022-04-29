import sys
sys.path.append(r"C:\xampp\htdocs\project_ecommerce")

from modules.modules import *
from modules.clear import *

clear()

class Order(Modules):
    
    def __init__(self, order = []):
        self._order = order


    def calc_total(self, taxes = 0.07): # Añadir un select con la opción de elegir el porcentaje de impuestos
        return round(self.calc_subtotal() + (self.calc_subtotal() * taxes), 2)

    
    def calc_subtotal(self):
        subtotal = 0

        for elem in self._order:
            subtotal += (elem[1] * elem[2])
        
        return round(subtotal, 2)




order = Order([["item1", 4, 15.59], ["item2", 8, 25.99], ["item3", 2, 5.26]])

print(order.calc_total())
