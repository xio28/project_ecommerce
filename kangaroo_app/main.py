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

        # PANED FRAMES_______________________________________________________
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.logo_fr = tk.Frame(self.root)
        self.logo_fr.grid(row=0, column=0, sticky='news')
        self.form_fr = tk.Frame(self.root, bg=self.BG)
        self.form_fr.grid(row=0, column=1, sticky='news')

        # LOGO_______________________________________________________________
        self.logo = tk.PhotoImage(file=self._LOGO_PATH)
        self.logo_l = tk.Label(self.logo_fr, image=self.logo, bg=self.BG).pack()

        # SINGUP GUI_________________________________________________________
        self.username_label = tk.Label(self.form_fr, text="Username", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).pack(anchor=tk.W, padx=25)
        self.username_entry = tk.Entry(self.form_fr, textvariable=self.username, fg=self.FONT2, font=('Arial', 12))
        self.username_entry.pack(fill=tk.X, padx=25, pady=2)
        self.username_entry.focus_set()

        self.password_label = tk.Label(self.form_fr, text="Password", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).pack(anchor=tk.W, padx=25)
        self.password_entry = tk.Entry(self.form_fr, textvariable=self.password, fg=self.FONT2, font=('Arial', 12)).pack(fill=tk.X, padx=25, pady=2)

        self.email_label = tk.Label(self.form_fr, text="Email", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).pack(anchor=tk.W, padx=25)
        self.email_entry = tk.Entry(self.form_fr, fg=self.FONT2, font=('Arial', 12)).pack(fill=tk.X, padx=25, pady=2)

        self.contact_label = tk.Label(self.form_fr, text="Phone Number", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).pack(anchor=tk.W, padx=25)
        self.contact_entry = tk.Entry(self.form_fr, fg=self.FONT2, font=('Arial', 12)).pack(fill=tk.X, padx=25, pady=2)

        self.id_label = tk.Label(self.form_fr, text="DNI", bg=self.BG, fg=self.FONT1, font=('Arial', 14)).pack(anchor=tk.W, padx=25)
        self.id_entry = tk.Entry(self.form_fr, fg=self.FONT2, font=('Arial', 12)).pack(fill=tk.X, padx=25, pady=2)


class Launcher(SingInGui):
    
    def __init__(self):
        #singin = SingInGui()
        singup = SingupGui()
        tk.mainloop()

if __name__ == "__main__":
    main = Launcher()