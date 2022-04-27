from json import *
from clear import *

clear()

class Modules:

    def file_as_list(self):
        with open(self.__BIZUM_CRED_FILE, "r") as f:
            return [loads(credentials) for credentials in f.readlines()]


    def last_key(self):
        return 1 if len(self.__operation) == 0 else (list(self.__operation.keys())[-1]) + 1

