from modules.login_modules import *
from tkinter import messagebox

class GuiModules(LoginModules):
    
    # ERROR MESSAGES_________________________________
    def error_user_exists(self, username):
        pass

    def error_user_not_exists(self, username):
        pass

    # Login__________________________________________
    def log_in (self, usarname, password):
        messagebox.showinfo('Ok', 'USER LOGIN')

    def sing_up (self, username, password):
        messagebox.showinfo('OK', 'USER REGISTER')