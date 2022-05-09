from os import name

if name == "nt":
    COMMERCE = r"C:\xampp\htdocs\project_ecommerce\database\commerce.txt"
    CLIENTS = r"C:\xampp\htdocs\project_ecommerce\database\clients.txt"
    ORDERS = r"C:\xampp\htdocs\project_ecommerce\database\orders.txt"
    OPERATIONS = r"C:\xampp\htdocs\project_ecommerce\database\operations.txt"
    SUPPLIERS = r"C:\xampp\htdocs\project_ecommerce\database\suppliers.txt"
    PRODUCTS = r"C:\xampp\htdocs\project_ecommerce\database\products.txt"
    INVOICE = r"C:\xampp\htdocs\project_ecommerce\database\invoices.txt"
    PAYPAL = r"C:\xampp\htdocs\project_ecommerce\database\paypal.txt"
    BIZUM = r"C:\xampp\htdocs\project_ecommerce\database\bizum.txt"
    CARD = r"C:\xampp\htdocs\project_ecommerce\database\card.txt"

else:
    COMMERCE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/commerce.txt"
    CLIENTS = "/home/cfgs1/Documentos/repo/project_ecommerce/database/clients.txt"
    ORDERS = "/home/cfgs1/Documentos/repo/project_ecommerce/database/orders.txt"
    OPERATIONS = "/home/cfgs1/Documentos/repo/project_ecommerce/database/operations.txt"
    SUPPLIERS = "/home/cfgs1/Documentos/repo/project_ecommerce/database/suppliers.txt"
    PRODUCTS = "/home/cfgs1/Documentos/repo/project_ecommerce/database/products.txt"
    INVOICE = "/home/cfgs1/Documentos/repo/project_ecommerce/database/invoices.txt"
    PAYPAL = "/home/cfgs1/Documentos/repo/project_ecommerce/database/paypal.txt"
    BIZUM = "/home/cfgs1/Documentos/repo/project_ecommerce/database/bizum.txt"
    CARD = "/home/cfgs1/Documentos/repo/project_ecommerce/database/card.txt"
