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
import json

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
                if not line[username][lower_payment]:
                    return line['payment'][lower_payment]
                else:
                    if lower_payment == "paypal":
                        pass

        else:
            return False



class Card(Payment):
    
    def __init__(self, name, card_number, expiration_date, cvv):
        self.__name = name
        self.__card_number = card_number
        self.__expiration_date = expiration_date
        self.__cvv = cvv

    def save_payment_info(self):
        pass



class Bizum(Payment):

    def __init__(self):
        self.__send_bizum_gateway()


    def _check_credentials(self, tel_num, pin):
        cred_l = self.file_as_list(self.__BIZUM_CRED_FILE)

        for credentials in cred_l:
            if tel_num == credentials["phone"] and pin == credentials["pin"]:
                return True

        return False
        

    def __send_bizum_gateway(self):
        
        tel_num = input("Introduzca su número de teléfono: ")
        pin = input("Introduzca su PIN de bizum (4 dígitos): ")

        if self._check_credentials(tel_num, pin):
            return True
        
        return False

        

class PayPal(Payment):
    
    def __init__(self):
        self.__send_paypal_gateway()
        

    def file_as_list(self):
        with open(self.PAYMENTS_FILE, "r") as f:
            return [json.loads(credentials) for credentials in f.readlines()]


    def _check_credentials(self, email, password):
        cred_l = self.file_as_list(self.PAYMENTS_FILE)

        for credentials in cred_l:
            if email == credentials["email"] and password == credentials["password"]:
                return True

        return False


    def __send_paypal_gateway(self):
        
        email = input("Introduzca su email de paypal: ")
        password = input("Introduzca su contraseña de paypal: ")

        if self._check_credentials(email, password):
            return True
        
        return False
