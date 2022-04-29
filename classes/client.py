import sys

sys.path.append(r"C:\xampp\htdocs\project_ecommerce")

from modules.clear import *
from modules.modules import *
import json
from pymongo.mongo_client import MongoClient
from database.connect_db import *

clear()

class Client:

    JSON_FILE = r"C:\xampp\htdocs\project_ecommerce\database\client_info.json"

    def __init__(self, username, email, password, name, nid, address, contact, recommended, pets = {}, payments = {}):
        self._username = username
        self._email = email
        self.__password = password
        self._name = name
        self._nid = nid
        self._address = address
        self._contact = contact
        self._recommended = recommended
        self._pets = pets
        self._payments = payments
        self.user_info()
        # self._user_info = {}
        # self.add_to_json()
        # print(self._user_info)

    def __str__(self) -> str:
        pass


    def user_info(self):
        with open(self.JSON_FILE, "a") as f:
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

            line = f.write(json.dumps(user_info, indent=2) + '\n')
            line.update()

        


    
    def add_to_json(self):
        clients_info_file = file_as_list(self.JSON_FILE)

        with open("aux_info.txt", "w") as f:
            for clients_info in clients_info_file:
                f.write(json.dumps(clients_info, indent=2))


client1 = Client("ilos28", "holaMundo", "xiomara@gmail.com", "Siomara Alonso", "44444444T", {"street": "C/Torres 1, 2º D", "postal_code": "35017", "city": "Las Palmas de G.C."}, ["678678678", "696696696"], True, [{"species": "perro", "pet_name": "Robin", "birthdate": "06/03/2014"}, {"species": "gato", "pet_name": "Deny", "birthdate": "20/09/2009"}])
client2 = Client("carcoal", "holaMundo", "chris@gmail.com", "Chris Medina", "33333333T", {"street": "C/Vega 1, 3º D", "postal_code": "35022", "city": "Telde"}, ["645124753"], False, [{"species": "gato", "pet_name": "Vilma", "birthdate": "28/10/2020"}])


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


    


    
