from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.modules import *

class KangarooPlatform:

    def __init__(self, nif, ecommerce_name, address):
        self.__nif = nif
        self._ecommerce_name = ecommerce_name
        self._address = address

    