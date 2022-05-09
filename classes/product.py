from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.files import *
from modules.modules import *
from modules.clear import *

class Products:

    def __init__(self, id = 0, supplier = "", p_name = "", species = "", category = "", price = 0):
        self.id = id
        self.supplier = supplier
        self.p_name = p_name
        self.species = species
        self.category = category
        self.price = price


    def add_products_to_file(self, obj):
        try:
            write_json(obj, PRODUCTS)

        except (FileNotFoundError, IOError):
            write_json(obj, PRODUCTS)

    

    def get_item_price(self, p_name):
        products_file = file_as_list(PRODUCTS)
        price = 0

        for product in products_file:
            if product['p_name'] == p_name:
                price = product['price']

        return price



    def return_products(self):
        products_file = file_as_list(PRODUCTS)
        result = []

        for product in products_file:
            result.extend([product["p_name"], product['price']])
        
        return result

            



p = Products()
p1 = Products(1, "Isabel Román-Ariño", "Nature's Variety Original Medium Adult pollo 12kg", "perro", "pienso", 59.95)
p2 = Products(2, "Isabel Román-Ariño", "Salvaje Base Esterilizado pienso 12kg", "gato", "pienso", 24.95)
p3 = Products(3, "Isabel Román-Ariño", "Alpha Spirit Albóndigas de Ciervo con Romero", "perro", "comida húmeda", 2.99)
p4 = Products(4, "Camilo Verdú Sala", "Wellness Core Tender Cuts Chicken Selection", "gato", "comida húmeda", 6.39)
p5 = Products(5, "Araceli Concha Pi Guijarro", "Nayeco X-TRM Cronos Neón Limón arnés talla L", "perro", "arneses", 15.29)
p6 = Products(6, "Araceli Concha Pi Guijarro", "Sepicat Light Weight Extreme Fresh arena aglomerante ligera 16L", "gato", "arena", 14.99)

p.add_products_to_file(p1)
p.add_products_to_file(p2)
p.add_products_to_file(p3)
p.add_products_to_file(p4)
p.add_products_to_file(p5)
p.add_products_to_file(p6)
# print(p.return_products())
# print(p.get_item_price("Nature's Variety Original Medium Adult pollo 12kg"))
