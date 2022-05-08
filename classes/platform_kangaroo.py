from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.modules import *
from modules.clear import *
from modules.files import *

class KangarooPlatform:

    def __init__(self, nif = "", ecommerce_name = "", address = ""):
        self.nif = nif
        self.ecommerce_name = ecommerce_name
        self.address = address



    def add_commerce_to_file(self, obj):
        try:
            if check_if_file_empty(COMMERCE_FILE):
                write_json(obj, COMMERCE_FILE)
            
            else:
                print("El fichero ya contiene información del comercio.")
                return False
                
        except (FileNotFoundError, IOError):
            write_json(obj, COMMERCE_FILE)
    

    
    def return_commerce_info(self):
        commerce_info = file_as_list(COMMERCE_FILE)
        
        for info in commerce_info:
            for x in info:
                commerce_info = fr'''
{info['ecommerce_name']}
{info['nif']}
{info['address']['street']}
{info['address']['postal_code']}
{info['address']['city']}
                    '''

        return commerce_info
        


c = KangarooPlatform()
c1 = KangarooPlatform("G12453786", "Kangaroo", {"street": "C/ Matagalpa, 2", "postal_code": "35010", "city": "Las Palmas de Gran Canaria"})

# c.add_commerce_to_file(c1)
# print(c.return_commerce_info())
