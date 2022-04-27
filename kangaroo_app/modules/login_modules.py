from modules.basic_modules import *

class LoginModules(BasicModules):
    
    # RETURN IF USER EXISTS_________________________
    def _search4user(self, username):
        users = [user for user in self.json2list(self._USER_PATH) if user['username'] == username.lower()]
        return False if len(users) == 0 else True

    # CREATE USER___________________________________
    def _create_user(self, username, password):
        users = self.json2list(self._USER_PATH)
        users.append({"username":username, "password":password})
        self.overwrite(self._USER_PATH, users)