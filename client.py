from modules.clear import clear


class Client:

    def __init__(self, username, email, password, name, nid, address, contact, recommended):
        self._username = username
        self._email = email
        self.__password = password
        self._name = name
        self._nid = nid
        self._address = address
        self._contact = contact
        self._recommended = recommended
        self._pets = {}
        self._payments = {}


    


    
