from modules.clear import *
from modules.modules import *
from order import *
from client import *
import json

class Payment:

    def __init__(self):
        self.__operation = {}


    def __get_order_total_cost(self):
        self.__operation = {
            self.last_key(): [self._username, self._calc_total()]
            }


class Card:
    
    def __init__(self, name, card_number, expiration_date, cvv):
        self.__name = name
        self.__card_number = card_number
        self.__expiration_date = expiration_date
        self.__cvv = cvv



class Bizum:

    __BIZUM_CRED_FILE = "bizum_credentials.txt"
    
    def __init__(self):
        self.__send_bizum_gateway()


    def _check_credentials(self, tel_num, pin):
        cred_l = self.file_as_list()

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

        

class PayPal:

    __PAYPAL_CRED_FILE = "paypal_credentials.txt"

    
    def __init__(self):
        self.__send_paypal_gateway()
        

    def file_as_list(self):
        with open(self.__PAYPAL_CRED_FILE, "r") as f:
            return [json.loads(credentials) for credentials in f.readlines()]


    def _check_credentials(self, email, password):
        cred_l = self.file_as_list()

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
