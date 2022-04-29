from bson import ObjectId
import sys
sys.path.append(r"C:\xampp\htdocs\project_ecommerce")

from pymongo.mongo_client import MongoClient
from os import name, system

def clear():
    return system('cls') if name == 'nt' else system('clear')

clear()

client_db = MongoClient('localhost', 27017)
db = client_db.kangaroo_db

