from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.modules import *


class Supplier:
    def __init__(self, nif, name, address, contact):
        self.__nif = nif
        self._name = name
        self._address = address
        self._contact = contact