from sys import path
from os import name
import datetime

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")


from classes.client import *
from classes.order import *
from classes.platform_kangaroo import *
from modules.modules import *
from modules.clear import *
from modules.files import *

today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

clear()


class Invoice:
    def __init__(self, user_info = {}, commerce_info = {}, order = [], datetime = ""):
        self.id = auto_key(INVOICE)
        self.user_info = user_info
        self.commerce_info = commerce_info
        self.order = order
        self.datetime = datetime



    def gen_invoice(self, username, datetime):
        obj = Invoice(Client.return_client_info(self, username), KangarooPlatform.return_commerce_info(self), Order.get_order_l(self, username, datetime), today)

        write_json(obj, INVOICE)



# inv = Invoice()
# print(inv.gen_invoice("ilos28", "09-05-2022"))
