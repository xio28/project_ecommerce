import sys
sys.path.append(r"C:\xampp\htdocs\project_ecommerce")

from modules.clear import *
import json

# clear()


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
        self._user_info = {}


    def user_info(self):
        self._user_info = {
            "user": {
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
        }

        print(self._user_info)

    
    def add_to_json(self):
        with open(self.JSON_FILE, "w") as f:
            f.write(json.dumps(self._user_info, indent=2))


client1 = Client("ilos28", "holaMundo", "xiomara@gmail.com", "Siomara Alonso", "44444444T", {"street": "C/Torres 1, 2º D", "postal_code": "35017", "city": "Las Palmas de G.C."}, ["678678678", "696696696"], True, [{"species": "perro", "pet_name": "Robin", "birthdate": "06/03/2014"}, {"species": "gato", "pet_name": "Deny", "birthdate": "20/09/2009"}])

client2 = Client("carcoal", "holaMundo", "chris@gmail.com", "Chris Medina", "33333333T", {"street": "C/Vega 1, 3º D", "postal_code": "35022", "city": "Telde"}, ["645124753"], False, [{"species": "gato", "pet_name": "Vilma", "birthdate": "28/10/2020"}])

# client.user_info()
client1.user_info()
client2.user_info()
client1.add_to_json()
client2.add_to_json()


    


    
