import json
import pickle
import os
# from pathlib import Path

CLIENTS_FILE = r"C:\xampp\htdocs\project_ecommerce\database\client_info.txt"
# CLIENTS_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/client_info.txt"


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
        # return "/home/cfgs1/Documentos/repo/project_ecommerce/database/paypal.txt"
        return r"C:\xampp\htdocs\project_ecommerce\database\paypal.txt"

    elif payment.lower() == "bizum":
        # return "/home/cfgs1/Documentos/repo/project_ecommerce/database/bizum.txt"
        return r"C:\xampp\htdocs\project_ecommerce\database\bizum.txt"

    else:
        # return "/home/cfgs1/Documentos/repo/project_ecommerce/database/card.txt"
        return r"C:\xampp\htdocs\project_ecommerce\database\card.txt"        


def load_bin_file(filename):
    if check_if_file_not_empty(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)



def count_events(keyword, payment):

    # Cuenta el número de veces que determinado valor aparece en el diccionario, si es mayor que 1 es que ya existe.
    p_file = load_bin_file(get_file_payment(payment))
    dic = p_file.__dict__
    s = sum(value == keyword for value in dic.values())

    if s > 1:
        return False
    else:
        return True



def check_if_user_exists(username):
    try:
        clients_file = file_as_list(CLIENTS_FILE)

        for c_info in clients_file:
            if c_info['username'] == username:
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



def write_json(new_data, filename):
    try:
        with open(filename, 'a') as f:
            f.write(json.dumps(new_data) + '\n')

    except (FileNotFoundError, IOError):
        with open(filename, 'w') as f:
            f.write(json.dumps(new_data) + '\n')



def write_pickle(new_data, filename):
    try:
        with open(filename, 'ab') as f:
            f.write(pickle.dumps(new_data) + '\n')

    except (FileNotFoundError, IOError):
        with open(filename, 'wb') as f:
            f.write(pickle.dumps(new_data) + '\n')



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
