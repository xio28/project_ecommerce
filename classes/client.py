from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.clear import *
from modules.modules import *
from modules.files import *
# from database.connect_db import *

clear()

class Client:

    def __init__(self, id = 0, username = "", password = "", email = "", name = "", nid = "", address = {}, contact = [], recommended = False):
        self.id = id
        self.username = username
        self._password = password
        self._email = email
        self._name = name
        self._nid = nid
        self._address = address
        self._contact = contact
        self.recommended = recommended



    def add_user_info_to_file(self, username, obj):
        try:
            if not check_if_user_exists(username):
                write_json(obj, CLIENTS_FILE)

            else:
                print("El usuario  ya existe.")
                
        except (FileNotFoundError, IOError):
            write_json(obj, CLIENTS_FILE)



    def check_credentials_login(self, username, password):
        if check_if_user_exists(username):
            clients_info = file_as_list(CLIENTS_FILE)
            
            for info in clients_info:
                for x in info:
                    if info["username"] == username and info["_password"] == password:
                        return True

                    else:
                        print("Credenciales incorrectas.")
                        return False
        
        else:
            print("El usuario no existe.")



    def return_client_info(self, username):
        if check_if_user_exists(username):
            clients_info = file_as_list(CLIENTS_FILE)

            
            for info in clients_info:
                for x in info:
                    if info["username"] == username:
                        user_info = {
                            'name': info['_name'],
                            'nid': info['_nid'],
                            'address': info['_address']['street'],
                            'address': info['_address']['postal_code'],
                            'address': info['_address']['city']
                            }

                        return user_info

            return False

        else:
            print("El usuario no existe.")


    
    # db.clients.insert_one(user_info)

# client = Client()
# print(client.return_client_info("ilos28"))

# client1 = Client("ilos28", "holaMundo", "xiomara@gmail.com", "Siomara Alonso", "44444444T", {"street": "C/Torres 1, 2º D", "postal_code": "35017", "city": "Las Palmas de G.C."}, ["678678678", "696696696"])
# client2 = Client("carcoal", "adiosMundo", "chris@gmail.com", "Chris Medina", "33333333T", {"street": "C/Vega 1, 3º D", "postal_code": "35022", "city": "Telde"}, ["645124753"])



# client.add_user_info_to_file("ilos28", client1)
# client.add_user_info_to_file("carcoal", client2)
# client.check_credentials_login("ilos28", "holaMund")
# print(client.return_client_info("ilos28"))
