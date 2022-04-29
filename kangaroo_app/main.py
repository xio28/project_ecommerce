#!/usr/bin/python3

import tkinter as tk
from modules.gui_modules import *

class KangarooInterface(GuiModules):
    _TITLE = "Kangaroo | PetShop"
    _MIN_HEIGHT = 320
    _MIN_WIDTH = 380

    _LOGO_PATH = './img/kangaroo_300.png'

    # COLORS SCHEME___________________________________________
    BG = "#f3f3f3"
    FONT1 = "#004c4c"
    FONT2 = "#5d634f"
    BTN_BG = "#004c4c"
    BTN_HOVER = "#006666" #"#66b2b2"
    BTN_FG = "#ffffff"

    def _wd_configure(self):
        self.root = tk.Tk()
        self.root.title(self._TITLE)
        self.root.resizable(False, False)
        self.root.config(bg=self.BG)
        #self.root.eval('tk::PlaceWindow . center')


class SingInGui(KangarooInterface):

    def __init__(self):
        self._wd_configure()
        
        # VAR DECLARATION____________________________________________________
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # LOGO_______________________________________________________________
        self.logo = tk.PhotoImage(file=self._LOGO_PATH)
        self.logo_l = tk.Label(self.root, image=self.logo, bg=self.BG).pack()

        # LOGIN GUI__________________________________________________________
        self.username_label = tk.Label(self.root, text="Username", bg=self.BG, fg=self.FONT1, font=('Arial', 16)).pack(anchor=tk.W, padx=25)
        self.username_entry = tk.Entry(self.root, textvariable=self.username, fg=self.FONT2, font=('Arial', 14))
        self.username_entry.pack(fill=tk.X, padx=25, pady=10)
        self.username_entry.focus_set()

        self.password_label = tk.Label(self.root, text="Password", bg=self.BG, fg=self.FONT1, font=('Arial', 16)).pack(anchor=tk.W, padx=25)
        self.password_entry = tk.Entry(self.root, textvariable=self.password, fg=self.FONT2, font=('Arial', 14)).pack(fill=tk.X, padx=25)

        self.separator = tk.Label(self.root, bg=self.BG).pack(pady=15)

        self.singin_btn = tk.Button(self.root, text="Sing in", bg=self.BTN_BG, activebackground=self.BTN_HOVER, fg=self.BTN_FG, activeforeground=self.BTN_FG, font=('Arial', 13)).pack(fill=tk.X, padx=25, pady=5)
        self.singup_btn = tk.Button(self.root, text="Sing up", bg=self.BTN_BG, activebackground=self.BTN_HOVER, fg=self.BTN_FG, activeforeground=self.BTN_FG, font=('Arial', 13)).pack(fill=tk.X, padx=25)

        self.separator = tk.Label(self.root, bg=self.BG).pack(pady=15)


class SingupGui(KangarooInterface):

    def __init__(self):
        self._wd_configure()

        # VAR DECLARATION____________________________________________________
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
        # SingUp GUI_________________________________________________________
        self.title = tk.Label(self.root, text="Kangaroo | SingUp Form", bg=self.BTN_BG, fg=self.BTN_FG, font=('Arial Bold', 12)).grid(row=0, column=0, columnspan=4, sticky='we')
        self.separator = tk.Label(self.root, bg=self.BG).grid(row=1, column=0)
        self.username_label = tk.Label(self.root, text="Username", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).grid(row=2, column=0, columnspan=2, sticky='W', padx=20)
        
        self.username_entry = tk.Entry(self.root, fg=self.FONT2, font=('Arial', 12), width=30)
        self.username_entry.grid(row=3, column=0, columnspan=2, sticky='news', padx=20, pady=5)
        self.username_entry.focus_set()

        self.dni_label = tk.Label(self.root, text="DNI", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).grid(row=2, column=2, columnspan=2, sticky='W', padx=20)
        self.dni_entry = tk.Entry(self.root, fg=self.FONT2, font=('Arial', 12), width=30).grid(row=3, column=2, columnspan=2, sticky='news', padx=20, pady=5)

        self.name_label = tk.Label(self.root, text="First Name", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).grid(row=4, column=0, columnspan=2, sticky='W', padx=20)
        self.name_entry = tk.Entry(self.root, fg=self.FONT2, font=('Arial', 12)).grid(row=5, column=0, columnspan=2, sticky='news', padx=20, pady=5)

        self.l_name_label = tk.Label(self.root, text="Last Name", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).grid(row=4, column=2, columnspan=2, sticky='W', padx=20)
        self.l_name_entry = tk.Entry(self.root, fg=self.FONT2, font=('Arial', 12)).grid(row=5, column=2, columnspan=2, sticky='news', padx=20, pady=5)

        self.email_label = tk.Label(self.root, text="Email", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).grid(row=6, column=0, columnspan=2, sticky='W', padx=20)
        self.email_entry = tk.Entry(self.root, fg=self.FONT2, font=('Arial', 12)).grid(row=7, column=0, columnspan=2, sticky='news', padx=20, pady=5)

        self.contact_label = tk.Label(self.root, text="Contact Number", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).grid(row=6, column=2, columnspan=2, sticky='W', padx=20)
        self.contact_entry = tk.Entry(self.root, fg=self.FONT2, font=('Arial', 12)).grid(row=7, column=2, columnspan=2, sticky='news', padx=20, pady=5)

        self.addres_label = tk.Label(self.root, text="Addres", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).grid(row=8, column=0, columnspan=2, sticky='W', padx=20)
        self.addres_entry = tk.Entry(self.root, fg=self.FONT2, font=('Arial', 12)).grid(row=9, column=0, columnspan=2, sticky='news', padx=20, pady=5)

        self.password_label = tk.Label(self.root, text="Password", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).grid(row=8, column=2, columnspan=2, sticky='W', padx=20)
        self.password_entry = tk.Entry(self.root, fg=self.FONT2, font=('Arial', 12)).grid(row=9, column=2, columnspan=2, sticky='news', padx=20, pady=5)

        self.clear_btn = tk.Button(self.root, text="Clear", width=12, bg=self.BTN_BG, fg=self.BTN_FG, activebackground=self.BTN_HOVER, activeforeground=self.BTN_FG).grid(row=11, column=2, sticky="E", padx=10, pady=15)
        self.submit_btn = tk.Button(self.root, text="Submit", width=13, bg=self.BTN_BG, fg=self.BTN_FG, activebackground=self.BTN_HOVER, activeforeground=self.BTN_FG).grid(row=11, column=3, sticky="W", padx=10, pady=15)

class Launcher(SingInGui):
    
    def __init__(self):
        #singin = SingInGui()
        singup = SingupGui()
        tk.mainloop()

if __name__ == "__main__":
    main = Launcher()