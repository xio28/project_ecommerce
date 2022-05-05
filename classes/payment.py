import pickle
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
        payment_file = load_bin_file(get_file_payment(payment))
        dic = payment_file.__dict__

        if dic["_username"] == username:
            if payment.lower() == "bizum":
                pass

        else:
            self._get_credentials(self, username, payment)



    def _get_credentials(self, username, payment):
        payment_file = load_bin_file(get_file_payment(payment))
        l = []
        print(len(payment_file))

        for p in payment_file:
            dic = p.__dict__
            print(dic)
            # if dic["_username"] == username:
            #     if payment.lower() == "bizum":
            #         l.extend([dic["_phone"], dic["_pin"]])

            #     elif payment.lower() == "paypal":
            #         l.extend([dic["_email"], dic["_password"]])

            #     else:
            #         l.extend([dic["_name"], dic["_card_number"], dic["_expiration_date"], dic["_cvv"]])
            
            # return l



    def _add_payment_to_file(self, username, payment, *obj):
        if check_if_user_exists(username):
            l_obj = []
            l_obj.append(obj)
            # print(l_obj)

            try:
                # if count_events(username, payment):
                with open(get_file_payment(payment), 'ab') as f:
                    pickle.dump(l_obj, f)

                # else:
                    # return False

            except (FileNotFoundError, IOError):
                with open(get_file_payment(payment), 'wb') as f:
                    pickle.dump(l_obj, f)
                        
        else:
            return False



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
bizum_1 = Bizum("ilos28", "678678678", "0505")
bizum_2 = Bizum("carcoal", "678945123", "1111")
paypal = PayPal("ilos28", "xiomara@gmail.com", "holaMundo")
card = Card("ilos28", "Siomara Alonso", "8124145314781564", "02/26", "333")

bizum_f = r"C:\xampp\htdocs\project_ecommerce\database\bizum.txt"
paypal_f = r"C:\xampp\htdocs\project_ecommerce\database\paypal.txt"
card_f = r"C:\xampp\htdocs\project_ecommerce\database\card.txt"

l = [bizum_1, bizum_2]
# l.extend([bizum_1, bizum_2])
payment._add_payment_to_file("ilos28", "bizum", bizum_1, bizum_2)
# payment._add_payment_to_file("carcoal", "bizum", bizum_2)
# payment._add_payment_to_file("ilos28", "PAYPAL", paypal)
# payment._add_payment_to_file("ilos28", "card", card)
print(payment._get_credentials("carcoal", "bizum"))
# payment._check_credentials("ilos28", "card")
