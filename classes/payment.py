from sys import path
from os import name

if name == "nt":
    path.append(r"C:\xampp\htdocs\project_ecommerce")
else:
    path.append("/home/cfgs1/Documentos/repo/project_ecommerce")


from modules.clear import *
from modules.modules import *
import datetime

today = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

class Payment:

    def __init__(self, username = "", payment = "", datetime = "", total = 0):
        self.id = auto_key(OPERATIONS)
        self.username = username
        self.payment = payment
        self.datetime = datetime
        self.total = total


    def pay_order(self, username, datetime, payment, entry):
        orders_file = file_as_list(ORDERS)
        state = False
        total = 0
        
        with open(ORDERS, 'w') as f:
            for order in orders_file:
                if order['username'] == username and order['datetime'] == datetime and self.check_credentials(username, payment, entry):
                    order['state'] = True
                    state = True
                    total = order['total']
                
                else:
                    state = False
            
                f.write(json.dumps(order))
    

        if state:
            obj = Payment(username, payment, today, total)


        write_json(obj, OPERATIONS)




    def check_credentials(self, username, payment, entry):
        l1 = self.get_credentials(username, payment).sort()
        l2 = entry.sort()

        if user_in_payments_file(username, payment):
            if l1 == l2:
                return True
            
            else:
                print("Credenciales incorrectas. Por favor, asegúrese de que estén bien escritas.")
        
        else:
            print("No tiene credenciales asociadas a este método de pago. Por favor, añadalas primero al fichero para poder continuar con el pago.")

            return False



    def get_credentials(self, username, payment):
        payment_file = file_as_list(get_file_payment(payment))
        cred_l = []

        for credentials in payment_file:
            for x in credentials:
                if credentials["username"] == username:
                    if payment.lower() == "bizum":
                        cred_l.extend([credentials["_phone"], credentials["_pin"]])
                        break

                    elif payment.lower() == "paypal":
                        cred_l.extend([credentials["_email"], credentials["_password"]])
                        break

                    else:
                        cred_l.extend([credentials["_name"], credentials["_card_number"], credentials["_expiration_date"], credentials["_cvv"]])
                        break

                
        return cred_l



    # Añade objeto a la lista de métodos de pago correspondiente; payment = (bizum \ paypal \ card)
    def add_payment_to_file(self, username, payment, obj):
        if check_if_user_exists(username):
            try:
                if not user_in_payments_file(username, payment):
                    write_json(obj, get_file_payment(payment))
                
                else:
                    print("El usuario ya está en la lista.")
                    return False


            except (FileNotFoundError, IOError):
                write_json(obj, get_file_payment(payment))
                   
                        

    def payment_l(self):
        return ["paypal", "bizum", "tarjeta"]



class Card:
    
    def __init__(self, username, name, card_number, expiration_date, cvv):
        self.username = username
        self._name = name
        self._card_number = card_number
        self._expiration_date = expiration_date
        self._cvv = cvv



class PayPal:
    
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self._password = password
    


class Bizum:

    def __init__(self, username, phone, pin):
        self.username = username
        self._phone = phone
        self._pin = pin

        

payment = Payment()

# bizum_1 = Bizum("ilos28", "678678678", "0505")
# bizum_2 = Bizum("carcoal", "678945123", "1111")
# paypal = PayPal("ilos28", "xiomara@gmail.com", "holaMundo")
# card = Card("ilos28", "Siomara Alonso", "8124145314781564", "02/26", "333")

# payment.add_payment_to_file("ilos28", "bizum", bizum_1)
# payment.add_payment_to_file("carcoal", "bizum", bizum_2)
# payment.add_payment_to_file("ilos28", "PAYPAL", paypal)
# payment.add_payment_to_file("ilos28", "card", card)
# print(payment.get_credentials("ilos28", "paypal"))
# print(payment.get_credentials("ilos28", "bizum"))
print(payment.pay_order("ilos28", "09-05-2022", "bizum", ["678678678", "0505"]))
