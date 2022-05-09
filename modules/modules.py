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
    pass
    # info_file = file_as_list(filename)
    # n = 1
    # n_l = []
    
    # for x in info_file:
    #     if x['id'] == 0:
    #         if info_file.index(x) == 0:
    #             x['id'] = n
    #             n_l.append(x)
            
    #         else:
    #             x['id'] += n
    #             n_l.append(x)
        
    #     n += 1
    
    # with open(filename, 'w') as f:
    #     for x in n_l:
    #         for n in x:
    #             print(n)
                # if x['id'] == 0:
                #     f.write(json.dumps(x) + "\n")
                # else:
                #     return False
    
    # return n_l
    # return 1 if l_dict[0]['id'] == 0 else l_dict[-1]['id'] + 1


# print(auto_key(PRODUCTS))

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



# def check_id(id, filename):
#     filename = file_as_list(filename)
    
#     for info in filename:
#         for x in info:
#             if info['id'] == id:
#                 return True
        
#     return False



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
