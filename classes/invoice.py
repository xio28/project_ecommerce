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
    def __init__(self, invoice = {}):
        self.invoice = invoice



    def gen_invoice(self, id, username, datetime):

        invoice = {
            "id": id,
            "user_info": Client.return_client_info(self, username),
            "commerce_info": KangarooPlatform.return_commerce_info(self),
            "order": Order.get_order_l(self, username, datetime),
            "datetime": today
        }

        obj = Invoice(invoice)

        write_json(obj, INVOICE)



inv = Invoice()

print(inv.gen_invoice(1, "ilos28", "09-05-2022"))
