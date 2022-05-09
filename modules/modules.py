from os import name
from sys import path

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")

import json
from modules.files import *
from modules.clear import *

clear()

def file_as_list(filename):
    with open(filename, "r") as f:
        return [json.loads(x) for x in f.readlines()]

        

def auto_key(filename):
    info_file = file_as_list(filename)

    if len(info_file) != 0:
        last_key = info_file[-1]['id']
        return last_key +1

    else:
        return 1


def get_file_payment(payment):
    if payment.lower() == "paypal":
        return PAYPAL

    elif payment.lower() == "bizum":
        return BIZUM

    else:
        return CARD 



def check_if_user_exists(username):
    try:
        clients_file = file_as_list(CLIENTS)

        for c_info in clients_file:
            if c_info['username'] == username:
                return True
        
        return False

    except (FileNotFoundError, IOError):
        return False



def user_in_payments_file(username, payment):
    try:
        payments_file = file_as_list(get_file_payment(payment))

        for user in payments_file:
            for x in user:
                if user['username'] == username:
                    return True
            
        return False

    except (FileNotFoundError, IOError):
        return False



def user_in_file(username, filename):
    try:
        filename = file_as_list(filename)

        for user in filename:
            for x in user:
                if user['username'] == username:
                    return True
            
        return False

    except (FileNotFoundError, IOError):
        return False



def get_client_info(username, key):
    if check_if_user_exists(username):
        clients_file = file_as_list(CLIENTS)

        for info in clients_file:
            if info['username'] == username:
                return info[key]



def write_json(obj, filename):
    try:
        with open(filename, 'a') as f:
            f.write(json.dumps(obj.__dict__) + '\n')

    except (FileNotFoundError, IOError):
        with open(filename, 'w') as f:
            f.write(json.dumps(obj.__dict__) + '\n')



def check_if_file_empty(filename):
    if os.path.getsize(filename) > 0:
        return False
    else:
        return True
    



