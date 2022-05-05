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

class Payment:

    # PAYMENTS_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/payments_info.txt"
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
        payment_file = load_bin_file(self.PAYMENTS_FILE)
        dic = payment_file.__dict__

        if dic["_username"] == username:
            if payment.lower() == "bizum":
                pass

        else:
            self._get_credentials(self, self.PAYMENTS_FILE, username, payment)



    def _get_credentials(self, filename, username, payment):
        payment_file = load_bin_file(filename)
        dic = payment_file.__dict__
        l = []

        if dic["_username"] == username:
            if payment.lower() == "bizum":
                l.extend([dic["_phone"], dic["_pin"]])

            elif payment.lower() == "paypal":
                l.extend([dic["_email"], dic["_password"]])

            else:
                l.extend([dic["_name"], dic["_card_number"], dic["_expiration_date"], dic["_cvv"]])
        
        return l



    def _add_payment_to_file(self, username, obj):

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

print(payment._add_payment_to_file("ilos28", bizum))
print(payment._add_payment_to_file("ilos28", paypal))
print(payment._add_payment_to_file("ilos28", card))
# print(payment.see_file(aux_file, "ilos28"))
