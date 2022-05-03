from json import *
from os import stat
from pathlib import Path
# from clear import *

# CLIENTS_FILE = r"C:\xampp\htdocs\project_ecommerce\database\client_info.txt"
CLIENTS_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/client_info.txt"


def file_as_list(file):
    with open(file, "r") as f:
        return [loads(x) for x in f.readlines()]



def last_key(dict):
    if not bool(dict):
        return dict.get('id', 1)
    else:
        return dict.get('id') + 1



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
            f.write(dumps(new_data) + '\n')

    except (FileNotFoundError, IOError):
        with open(filename, 'w') as f:
            f.write(dumps(new_data) + '\n')



def if_file_exists(filename):
    my_file = Path(filename)
    
    return my_file.is_file()



def check_if_file_empty(filename):
    if stat(filename) == 0:
        return True
    else:
        return False
    

# Comprueba si una condición (nombre, número, etc.) está dentro del diccionario
def check_key_condition(key, condition, filename):
    try:
        file_data = file_as_list(filename)

        with open(filename, 'r') as f:
            for data in file_data:
                if data[key] == condition:
                    return True
            
            return False

    except (FileNotFoundError, IOError):
        return False
