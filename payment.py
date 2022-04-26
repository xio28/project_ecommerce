from os import system, name
from abc import ABC, abstractmethod

if name == "nt":
    system('cls')
else:
    system('clear')


class Payment(ABC):

    def __init__(self):
        pass


class Card:
    pass

class Bizum:
    pass

class PayPal:
    pass
