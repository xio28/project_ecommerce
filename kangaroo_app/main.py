#!/usr/bin/python3

from tkinter import *
from modules.gui_modules import *

"""
    This file is only a test for GUI
"""

class Login(GuiModules):
    __TITLE = "Kangaroo | PetShop"
    __MIN_HEIGHT = 320
    __MIN_WIDTH = 380

    _LOGO_PATH = './img/kangaroo_2.png'

    # COLORS SCHEME___________________________________________
    BG = "#f3f3f3" #"#9ccc04"
    FONT1 = "#004c4c"
    FONT2 = "#5d634f"
    BTN_BG = "#004c4c"
    BTN_HOVER = "#66b2b2"
    BTN_FG = "#ffffff"

    def __init__(self):
        self._login()

    def _login(self):
        self.root = Tk()
        self.root.title(self.__TITLE)
        #self.root.minsize(self.__MIN_HEIGHT, self.__MIN_WIDTH)
        self.root.resizable(False, False)
        self.root.config(bg=self.BG)

        # VAR DECLARATIONS____________________________________
        username = StringVar()
        password = StringVar()

        # LOGO________________________________________________
        self.logo = PhotoImage(file=self._LOGO_PATH)

        # LOGIN GUI___________________________________________
        self.logo_l = Label(self.root, image=self.logo, bg=self.BG).pack()

        self.username_label = Label(self.root, text="Username", bg=self.BG, fg=self.FONT1, font=('Arial', 16)).pack(anchor=W, padx=25)
        self.username_entry = Entry(self.root, textvariable=username, fg=self.FONT2, font=('Arial', 14))
        self.username_entry.pack(fill=X, padx=25)
        self.username_entry.focus_set()

        self.password_label = Label(self.root, text="Password", bg=self.BG, fg=self.FONT1, font=('Arial', 16)).pack(anchor=W, padx=25)
        self.password_entry = Entry(self.root, textvariable=password, fg=self.FONT2, font=('Arial', 14)).pack(fill=X, padx=25)

        self.separator = Label(self.root, bg=self.BG).pack(pady=15)

        self.login = Button(self.root, text="Login", bg=self.BTN_BG, fg=self.BTN_FG, activebackground=self.BTN_HOVER, font=('Arial', 13), command=lambda:self.log_in(username, password)).pack(fill=X, padx=25)
        self.singup = Button(self.root, text="Sing in", bg=self.BTN_BG, fg=self.BTN_FG, activebackground=self.BTN_HOVER, font=('Arial', 13), command=lambda:self.sing_up(username, password)).pack(fill=X, padx=25, pady=10)

        self.separator = Label(self.root, bg=self.BG).pack(pady=15)

        # MAINLOOP____________________________________________
        self.root.mainloop()

class SingIn(GuiModules):
    __TITLE = "Kangaroo | PetShop"
    __MIN_HEIGHT = 320
    __MIN_WIDTH = 380

    _LOGO_PATH = './img/kangaroo_2.png'

    # COLORS SCHEME___________________________________________
    BG = "#f3f3f3" #"#9ccc04"
    FONT1 = "#004c4c"
    FONT2 = "#5d634f"
    BTN_BG = "#004c4c"
    BTN_HOVER = "#66b2b2"
    BTN_FG = "#ffffff"

    def __init__(self):
        self._singin()

    def _singin(self):
        self.root = Tk()
        self.root.title(self.__TITLE)
        self.root.resizable(False, False)
        self.root.config(bg=self.BG)

        # VAR DECLARATION____________________
        username = StringVar()
        password = StringVar()

        # Singup GUI_________________________
        self.title = Label(self.root, text="Sing Up", bg=self.BG, fg=self.FONT1).pack(anchor=CENTER, pady=20)

        # MAINLOOP___________________________
        self.root.mainloop()


class KangarooAdmin():
    pass

class Kangaroo():
    pass

class Launcher():
    pass


if __name__ == "__main__":
    login = SingIn()