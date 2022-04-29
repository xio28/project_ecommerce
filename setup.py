import sys
from os import name

if name == "nt":
    sys.path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    sys.path.append("/home/1cfgs/...")
