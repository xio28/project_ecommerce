from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.modules import *


class Supplier:
    def __init__(self, nif = "", name = "", address = "", contact = ""):
        self.nif = nif
        self.name = name
        self.address = address
        self.contact = contact



    def add_supplier_to_file(self, obj):
        try:
            write_json(obj, SUPPLIERS)

        except (FileNotFoundError, IOError):
            write_json(obj, SUPPLIERS)



s = Supplier()
s1 = Supplier(1, "28769037Q", "Isabel Román-Ariño", "C/Libertad, 68, 04869, Almería", "750756063")
s2 = Supplier(2, "19652938J", "Camilo Verdú Sala", "C/Rúa de San Pedro, 96, 37830, Salamanca", "660340815")
s3 = Supplier(3, "12590367Y", "Araceli Concha Pi Guijarro", "C/Manuel Iradier, 42, 03770, Alicante", "673771979")


# s.add_supplier_to_file(s1)
# s.add_supplier_to_file(s2)
# s.add_supplier_to_file(s3)
