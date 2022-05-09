from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")


from product import *
from modules.modules import *
from modules.clear import *
import datetime
# from database.connect_db import *

today = datetime.datetime.now().strftime("%d-%m-%Y")

clear()

class Order:
    
    def __init__(self, username = "", order = [], datetime = ""):
        self.id = auto_key(ORDERS)
        self.username = username
        self.order = order
        self.datetime = datetime
        self.total = self.calc_total()
        self.state = False



    def add_order_to_file(self, username, obj):
        if check_if_user_exists(username):
            write_json(obj, ORDERS)
                



    def calc_total(self, taxes = 0.07):
        return round(self.calc_subtotal() + (self.calc_subtotal() * taxes), 2)

    
    def calc_subtotal(self):
        subtotal = 0

        for elem in self.order:
            subtotal += (elem[1] * elem[2])
        
        return round(subtotal, 2)



    def get_order_l(self, username, datetime):
        orders_file = file_as_list(ORDERS)

        for order in orders_file:
            for x in order:
                if order['username'] == username and order['datetime'] == datetime:
                    print(order)
                    return True





# order = Order("ilos28", [["Nature's Variety Original Medium Adult pollo 12kg", 1, 59.95], ["Salvaje Base Esterilizado pienso 12kg", 1, 24.95], ["Alpha Spirit Albóndigas de Ciervo con Romero", 3, 2.99]], today)
# order.add_order_to_file("ilos28", order)
# order.get_items_to_cart("Nature's Variety Original Medium Adult pollo 12kg", 1)
# order.get_items_to_cart("Salvaje Base Esterilizado pienso 12kg", 1)

# print(order.calc_total())
# o = Order()
# print(o.get_order_l("ilos28", "09-05-2022"))
