from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.clear import *
from modules.modules import *
from database.connect_db import *

clear()

class Client:

    JSON_FILE = r"C:\xampp\htdocs\project_ecommerce\database\client_info.txt"
    # JSON_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/client_info.txt"

    def __init__(self, username, email, password, name, nid, address, contact):
        self._username = username
        self._email = email
        self.__password = password
        self._name = name
        self._nid = nid
        self._address = address
        self._contact = contact
        self.store_user_info()


    def store_user_info(self):
        user_info = {
            "username": self._username,
            "email": self._email,
            "password": self.__password,
            "name": self._name,
            "NID": self._nid,
            "phone": self._contact,
            "address": self._address
        }

        write_json(user_info, self.JSON_FILE, "username", self._username)
        db.clients.insert_one(user_info)


client1 = Client("ilos28", "holaMundo", "xiomara@gmail.com", "Siomara Alonso", "44444444T", {"street": "C/Torres 1, 2º D", "postal_code": "35017", "city": "Las Palmas de G.C."}, ["678678678", "696696696"])
client2 = Client("carcoal", "holaMundo", "chris@gmail.com", "Chris Medina", "33333333T", {"street": "C/Vega 1, 3º D", "postal_code": "35022", "city": "Telde"}, ["645124753"])


    


    
