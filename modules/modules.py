from json import *
from os import stat
# from clear import *

CLIENT_INFO = r"C:\xampp\htdocs\project_ecommerce\database\client_info.txt"

def file_as_list(file):
    with open(file, "r") as f:
        return [loads(x) for x in f.readlines()]


def last_key(dict):
    if not bool(dict):
        return dict.get('id', 1)
    else:
        return dict.get('id') + 1


d = {'id': 1}
print(last_key(d))


def test_funct():
    clients_file = file_as_list(CLIENT_INFO)

    for x in clients_file:
        pass

def check_if_user_exists(username):
    clients_file = file_as_list(CLIENT_INFO)

    for c_info in clients_file:
        if c_info['username'] == username:
            return True
    
    return False
        


d = {"id": 1, "username": "caracol"}
print(last_key(d))

def write_json(new_data, filename, key, condition):
    try:
        with open(filename, 'a') as f:
            if check_key_condition(key, condition, filename):
                print(f"El {key} {condition} ya existe.")
                return False
            else:
                f.write(dumps(new_data) + '\n')

    except (FileNotFoundError, IOError):
        with open(filename, 'w') as f:
            f.write(dumps(new_data) + '\n')


def check_if_file_empty(filename):
    if stat(filename) == 0:
        return True
    else:
        return False
    

# Comprueba si una condición (nombre, número, etc.) está dentro del diccionario
def check_key_condition(key, condition, filename):
    file_data = file_as_list(filename)

    with open(filename, 'r') as f:
        for data in file_data:
            if data[key] == condition:
                return True
        
        return False
