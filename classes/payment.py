import json
import pickle
from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.clear import *
from modules.modules import *
from order import *
from client import *

aux_file = "/home/cfgs1/Documentos/repo/project_ecommerce/classes/aux_file.txt"

class Payment:

    PAYMENTS_FILE = r"C:\xampp\htdocs\project_ecommerce\database\payments_info.txt"

    def __init__(self):
        self._operation = {}


    def _get_order_total_cost(self, username):
        operation_file = file_as_list()

        self._operation = {
            'id': last_key(operation_file),
            'order': [username, self.calc_total()], 
            'payment': ''
            }


    def _check_credentials(self, username, payment):
        if check_if_user_exists(username):
            lower_payment = payment.lower()
            payment_file = file_as_list(self.PAYMENTS_FILE)

            for line in payment_file:
                if not line[username][lower_payment]: # Si la lista está vacía
                    return False

                else:
                    return line[username][lower_payment]

        else:
            return False

    def load_bin_file(self, filename):
        l = []
        if os.path.getsize(filename) > 0:
            with open(filename, "rb") as f:
                l = pickle.load(f)

        return l

    def see_file(self, filename, username, payment):
        file = self.load_bin_file(filename)
        dic = file.__dict__
        l = []
        if dic["_username"] == username:
            if payment == "bizum":
                l.extend([dic["_phone"], dic["_pin"]])

            elif payment == "paypal":
                l.extend([dic["_email"], dic["_password"]])

            else:
                l.extend([dic["_name"], dic["_card_number"], dic["_expiration_date"], dic["_cvv"]])
        
        return l



    def add_payment_to_file(self, username, obj):

        if check_if_user_exists(username):

            try:
                with open(self.PAYMENTS_FILE, 'ab') as f:
                    pickle.dump(obj, f)

            except (FileNotFoundError, IOError):
                with open(self.PAYMENTS_FILE, 'wb') as f:
                    pickle.dump(obj, f)
                        
        else:
            return False


    # Añadir función "devolver métodos de pago"
    def _return_payment(self):
        pass



class Card:
    
    def __init__(self, username, name, card_number, expiration_date, cvv):
        self._username = username
        self._name = name
        self._card_number = card_number
        self._expiration_date = expiration_date
        self._cvv = cvv

    
    def get_card_info(self):
        pass


class PayPal:
    
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password
    


class Bizum:

    def __init__(self, username, phone, pin):
        self._username = username
        self._phone = phone
        self._pin = pin

        

payment = Payment()
bizum = Bizum("ilos28", "678678678", "0505")
paypal = PayPal("ilos28", "xiomara@gmail.com", "holaMundo")
card = Card("ilos28", "Siomara Alonso", "8124145314781564", "02/26", "333")

print(payment.add_payment_to_file("ilos28", bizum))
print(payment.add_payment_to_file("ilos28", paypal))
print(payment.add_payment_to_file("ilos28", card))
print(payment.see_file(aux_file, "ilos28"))
