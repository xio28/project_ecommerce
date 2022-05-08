from sys import path
from os import name

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


clear()
class Invoice:
    def __init__(self, id = 0):
        self.id = id


    def gen_invoice(self, username):
        result = f'''
INVOICE Nº {self.id}

{Client.return_client_info(self, username)} | {KangarooPlatform.return_commerce_info(self)}

Uds | Nº Arts | Artículo | Precio Unidad | Precio Total

        '''
        
        return result


inv = Invoice()

print(inv.gen_invoice("ilos28"))
