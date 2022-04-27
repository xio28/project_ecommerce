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

    # COLORS SCHEME___________________________________________
    BG = "#9ccc04"
    FONT1 = "#3c413c"
    FONT2 = "#5d634f"
    BTN_BG = "#87857e"
    BTN_FG = "#ffffff"

    def __init__(self):
        self._login()

    def _login(self):
        self.root = Tk()
        self.root.title(self.__TITLE)
        self.root.minsize(self.__MIN_HEIGHT, self.__MIN_WIDTH)
        self.root.resizable(False, False)
        self.root.config(bg=self.BG)

        # VAR DECLARATIONS____________________________________
        username = StringVar()
        password = StringVar()

        # LOGIN GUI___________________________________________
        self.title = Label(self.root, text="Kangaroo", bg=self.BG, fg=self.FONT1, font=('Arial Bold', 24)).pack(anchor=CENTER, pady=30)

        self.username_label = Label(self.root, text="Username", bg=self.BG, fg=self.FONT1, font=('Arial', 16)).pack(anchor=W, padx=25)
        self.username_entry = Entry(self.root, textvariable=username, fg=self.FONT2, font=('Arial', 14))
        self.username_entry.pack(fill=X, padx=25)
        self.username_entry.focus_set()

        self.password_label = Label(self.root, text="Password", bg=self.BG, fg=self.FONT1, font=('Arial', 16)).pack(anchor=W, padx=25)
        self.password_entry = Entry(self.root, textvariable=password, fg=self.FONT2, font=('Arial', 14)).pack(fill=X, padx=25)

        self.separator = Label(self.root, bg=self.BG).pack(pady=15)

        self.login = Button(self.root, text="Login", bg=self.BTN_BG, fg=self.BTN_FG, font=('Arial', 13), command=lambda:self.log_in(username, password)).pack(fill=X, padx=25, pady=5)
        self.singup = Button(self.root, text="Sing up", bg=self.BTN_BG, fg=self.BTN_FG, font=('Arial', 13), command=lambda:self.sing_up(username, password)).pack(fill=X, padx=25)

        # MAINLOOP____________________________________________
        self.root.mainloop()

class KangarooAdmin():
    pass

class Kangaroo():
    pass

class Launcher():
    pass


if __name__ == "__main__":
    login = Login()