from connect_db import *

mydb = db.kangaroo_db
mycol = mydb.clients

for x in mycol.find():
    print(x)

# x = db.clients.find_one()

# print(x)
