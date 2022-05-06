# import pickle
import json
from sys import path

path.append(r"C:\xampp\htdocs\project_ecommerce")
# path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

from modules.clear import *
from modules.modules import *
from order import *
from client import *

class Payment:

    # PAYMENTS_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/payments_info.txt"
    # PAYMENTS_FILE = r"C:\xampp\htdocs\project_ecommerce\database\payments_info.txt"

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
        payment_file = file_as_list(get_file_payment(payment))

        for cred in payment_file:
            if cred["_username"] == username:
                if payment.lower() == "bizum":
                    pass

            else:
                self._get_credentials(self, username, payment)



    def _get_credentials(self, username, payment):
        payment_file = file_as_list(get_file_payment(payment))
        l = []

        for credentials in payment_file:
            for x in credentials:
                if credentials["username"] == username:
                    if payment.lower() == "bizum":
                        l.extend([credentials["_phone"], credentials["_pin"]])
                        break

                    elif payment.lower() == "paypal":
                        l.extend([credentials["_email"], credentials["_password"]])
                        break

                    else:
                        l.extend([credentials["_name"], credentials["_card_number"], credentials["_expiration_date"], credentials["_cvv"]])
                        break
                
        return l



    def _add_payment_to_file(self, username, payment, obj):
        if check_if_user_exists(username):

            try:
                if not user_in_payments_file(username, payment):
                    write_json(obj, get_file_payment(payment))
                
                else:
                    print("El usuario ya está en la lista.")
                    return False


            except (FileNotFoundError, IOError):
                write_json(obj, get_file_payment(payment))
                        



class Card:
    
    def __init__(self, username, name, card_number, expiration_date, cvv):
        self.username = username
        self._name = name
        self._card_number = card_number
        self._expiration_date = expiration_date
        self._cvv = cvv

    
    def get_card_info(self):
        pass


class PayPal:
    
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self._password = password
    


class Bizum:

    def __init__(self, username, phone, pin):
        self.username = username
        self._phone = phone
        self._pin = pin

        

payment = Payment()
bizum_1 = Bizum("ilos28", "678678678", "0505")
bizum_2 = Bizum("carcoal", "678945123", "1111")
paypal = PayPal("ilos28", "xiomara@gmail.com", "holaMundo")
card = Card("ilos28", "Siomara Alonso", "8124145314781564", "02/26", "333")

bizum_f = r"C:\xampp\htdocs\project_ecommerce\database\bizum.txt"
paypal_f = r"C:\xampp\htdocs\project_ecommerce\database\paypal.txt"
card_f = r"C:\xampp\htdocs\project_ecommerce\database\card.txt"

payment._add_payment_to_file("ilos28", "bizum", bizum_1)
# payment._add_payment_to_file("carcoal", "bizum", bizum_2)
# payment._add_payment_to_file("ilos28", "PAYPAL", paypal)
# payment._add_payment_to_file("ilos28", "card", card)
# print(payment._get_credentials("carcoal", "bizum"))
# payment._check_credentials("ilos28", "card")
