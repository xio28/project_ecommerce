import json
import pickle
import os
# from pathlib import Path

# CLIENTS_FILE = r"C:\xampp\htdocs\project_ecommerce\database\client_info.txt"
CLIENTS_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/client_info.txt"


def file_as_list(filename):
    with open(filename, "r") as f:
        return [json.loads(x) for x in f.readlines()]



def last_key(dict):
    if not bool(dict):
        return dict.get('id', 1)
    else:
        return dict.get('id') + 1



def get_file_payment(payment):
    if payment.lower() == "paypal":
        return "/home/cfgs1/Documentos/repo/project_ecommerce/database/paypal.txt"
        # return r"C:\xampp\htdocs\project_ecommerce\database\paypal.txt"

    elif payment.lower() == "bizum":
        return "/home/cfgs1/Documentos/repo/project_ecommerce/database/bizum.txt"
        # return r"C:\xampp\htdocs\project_ecommerce\database\bizum.txt"

    else:
        return "/home/cfgs1/Documentos/repo/project_ecommerce/database/card.txt"
        # return r"C:\xampp\htdocs\project_ecommerce\database\card.txt"        



def check_if_user_exists(username):
    try:
        clients_file = file_as_list(CLIENTS_FILE)

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
        clients_file = file_as_list(CLIENTS_FILE)

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



# def if_file_exists(filename):
#     my_file = Path(filename)
    
#     return my_file.is_file()



def check_if_file_not_empty(filename):
    if os.path.getsize(filename) > 0:
        return True
    else:
        return False
    

# Comprueba si una condición (nombre, número, etc.) está dentro del diccionario
# def check_key_condition(key, condition, filename):
#     try:
#         file_data = file_as_list(filename)

#         with open(filename, 'r') as f:
#             for data in file_data:
#                 if data[key] == condition:
#                     return True
            
#             return False

#     except (FileNotFoundError, IOError):
#         return False

# count_events("ilos28", "bizum")
