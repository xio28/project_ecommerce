from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.clear import *
from modules.modules import *
import json
# from pymongo.mongo_client import MongoClient
# from database.connect_db import *

clear()

class Client:

    # JSON_FILE = r"C:\xampp\htdocs\project_ecommerce\database\client_info.json"
    JSON_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/client_info.json"

    def __init__(self, username, email, password, name, nid, address, contact, payments = {}):
        self._username = username
        self._email = email
        self.__password = password
        self._name = name
        self._nid = nid
        self._address = address
        self._contact = contact
        self._payments = payments
        # self.user_info()


    def add_to_db(self):
        with open(self.JSON_FILE, "r+") as f:
            user_info = {
                # "_id": last_key(self._user_info),
                "username": self._username,
                "email": self._email,
                "password": self.__password,
                "name": self._name,
                "NID": self._nid,
                "phone": self._contact,
                "recommended": self._recommended,
                "address": self._address,
                "pets": self._pets,
                "payments": self._payments
            }

            write_json(user_info, self.JSON_FILE)




# client1 = Client("ilos28", "holaMundo", "xiomara@gmail.com", "Siomara Alonso", "44444444T", {"street": "C/Torres 1, 2º D", "postal_code": "35017", "city": "Las Palmas de G.C."}, ["678678678", "696696696"])
# client2 = Client("carcoal", "holaMundo", "chris@gmail.com", "Chris Medina", "33333333T", {"street": "C/Vega 1, 3º D", "postal_code": "35022", "city": "Telde"}, ["645124753"])

user_exists("hola", "/home/cfgs1/Documentos/repo/project_ecommerce/database/client_info.json")
# client1.user_info()
# client2.user_info()
# clients_db = [client1, client2]

# result = db.clients.insert_many(clients_db.__dict__)

# print('Éxito al insertar')
# print(result)

# client.user_info()
# client1.user_info()
# client2.user_info()
# client1.add_to_json()
# client2.add_to_json()


    


    
