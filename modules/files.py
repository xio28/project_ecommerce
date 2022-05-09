from os import name

if name == "nt":
    COMMERCE_FILE = r"C:\xampp\htdocs\project_ecommerce\database\commerce_info.txt"
    CLIENTS_FILE = r"C:\xampp\htdocs\project_ecommerce\database\clients_info.txt"
    ORDERS_FILE = r"C:\xampp\htdocs\project_ecommerce\database\orders_info.txt"
    OPERATIONS = r"C:\xampp\htdocs\project_ecommerce\database\operations.txt"
    SUPPLIERS = r"C:\xampp\htdocs\project_ecommerce\database\suppliers.txt"
    PRODUCTS = r"C:\xampp\htdocs\project_ecommerce\database\products.txt"
    INVOICE = r"C:\xampp\htdocs\project_ecommerce\database\invoices.txt"
    PAYPAL = r"C:\xampp\htdocs\project_ecommerce\database\paypal.txt"
    BIZUM = r"C:\xampp\htdocs\project_ecommerce\database\bizum.txt"
    CARD = r"C:\xampp\htdocs\project_ecommerce\database\card.txt"

else:
    COMMERCE_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/commerce_info.txt"
    CLIENTS_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/clients_info.txt"
    ORDERS_FILE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/orders_info.txt"
    OPERATIONS = "/home/cfgs1/Documentos/repo/project_ecommerce/database/operations.txt"
    SUPPLIERS = "/home/cfgs1/Documentos/repo/project_ecommerce/database/suppliers.txt"
    PRODUCTS = "/home/cfgs1/Documentos/repo/project_ecommerce/database/products.txt"
    INVOICE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/invoices.txt"
    PAYPAL = "/home/cfgs1/Documentos/repo/project_ecommerce/database/paypal.txt"
    BIZUM = "/home/cfgs1/Documentos/repo/project_ecommerce/database/bizum.txt"
    CARD = "/home/cfgs1/Documentos/repo/project_ecommerce/database/card.txt"
