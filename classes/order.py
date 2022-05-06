from sys import path
# path.append(r"C:\xampp\htdocs\project_ecommerce")
path.append("/home/cfgs1/Documentos/repo/project_ecommerce")


from modules.modules import *
from modules.clear import *
# from database.connect_db import *

clear()

ORDERS_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/orders_info.txt"

class Order:
    
    def __init__(self, username = "", order = [], total = 0):
        self.username = username
        self._order = order
        self._total = self.calc_total()
        # self._orders_info = {}



    def add_order_to_file(self, username, obj):
        if check_if_user_exists(username):
            print("hola")
            try:
                if not user_in_file(username, ORDERS_FILE):
                    write_json(obj, ORDERS_FILE)
                
                else:
                    print("El usuario ya está en la lista.")
                    return False


            except (FileNotFoundError, IOError):
                write_json(obj, ORDERS_FILE)


    def gen_order_info(self):
        pass
        


    def calc_total(self, taxes = 0.07): # Añadir un select con la opción de elegir el porcentaje de impuestos
        return round(self.calc_subtotal() + (self.calc_subtotal() * taxes), 2)

    
    def calc_subtotal(self):
        subtotal = 0

        for elem in self._order:
            subtotal += (elem[1] * elem[2])
        
        return round(subtotal, 2)


order = Order("ilos28", [["item1", 4, 15.59], ["item2", 8, 25.99], ["item3", 2, 5.26]])
order.add_order_to_file("ilos28", order)

# print(order.calc_total())
