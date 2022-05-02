import os, json

class BasicModules():
    _USER_PATH = '../databases/users.txt'

    # CREATE DB IF NOT EXISTS______________________
    def _create_db_user(self):
        if not os.path.exists(self._USER_PATH):
            with open(self._USER_PATH, 'x') as f:
                pass

    
    # CONVERT JSON TO LIST_________________________ ****
    def _json2list(self, path):
        with open(path, 'r') as f:
            return [json.loads(data) for data in f.readlines()]

    
    # OVERWRITE THE FILE IN PATH___________________
    def _overwrite(self, path, content):
        with open('overwrite.txt', 'w') as f:
            for i in range(len(content)):
                if i == len(content) -1:
                    f.write(json.dumps(content[i]))
                else:
                    f.write(json.dumps(content[i]) + '\n')
        os.remove(path)
        os.rename('overwrite.txt', path)
