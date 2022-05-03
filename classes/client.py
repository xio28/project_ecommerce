from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.clear import *
from modules.modules import *
# from database.connect_db import *

clear()

class Client:

    CLIENTS_FILE = r"C:\xampp\htdocs\project_ecommerce\database\client_info.txt"
    PAYMENTS_FILE = r"C:\xampp\htdocs\project_ecommerce\database\payments_info.txt"
    # CLIENTS_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/client_info.txt"
    # PAYMENTS_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/payments_info.txt"

    def __init__(self, username, email, password, name, nid, address, contact):
        self._username = username
        self._email = email
        self.__password = password
        self._name = name
        self._nid = nid
        self._address = address
        self._contact = contact
        self.store_user_info()
        self.store_user_payment_info()


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

        try:
            if check_if_user_exists(self._username):
                print("El usuario ya existe.")
                return False
            else:
                write_json(user_info, self.CLIENTS_FILE)
                return True

        except (FileNotFoundError, IOError):
            write_json(user_info, self.CLIENTS_FILE)
            return True
            
    
    def store_user_payment_info(self):
        payment_info = {
            self._username: {
                "card": [],
                "paypal": [],
                "bizum": []
            }
        }
        
        if not self.store_user_info():
            write_json(payment_info, self.PAYMENTS_FILE)


        # db.clients.insert_one(user_info)


client1 = Client("ilos28", "holaMundo", "xiomara@gmail.com", "Siomara Alonso", "44444444T", {"street": "C/Torres 1, 2º D", "postal_code": "35017", "city": "Las Palmas de G.C."}, ["678678678", "696696696"])
client2 = Client("carcoal", "holaMundo", "chris@gmail.com", "Chris Medina", "33333333T", {"street": "C/Vega 1, 3º D", "postal_code": "35022", "city": "Telde"}, ["645124753"])
