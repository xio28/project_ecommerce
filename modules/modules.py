import json
import os
from modules.files import *



def file_as_list(filename):
    with open(filename, "r") as f:
        return [json.loads(x) for x in f.readlines()]

        

def last_key(l_dict):
    return 1 if l_dict[0]['id'] == 0 else l_dict[-1]['id'] + 1



def get_file_payment(payment):
    if payment.lower() == "paypal":
        return PAYPAL

    elif payment.lower() == "bizum":
        return BIZUM

    else:
        return CARD 



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



def check_if_file_empty(filename):
    if os.path.getsize(filename) > 0:
        return False
    else:
        return True
    

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
