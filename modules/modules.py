from json import *
# from clear import *

# clear()


def file_as_list(filename):
    with open(filename, "r") as f:
        return [loads(x) for x in f.readlines()]


def last_key(dict):
    return 1 if len(dict) == 0 else (list(dict)[-1]) + 1


def write_json(new_data, filename):
    with open(filename,'r+') as f:
        file_data = load(f)
        file_data.append(new_data)
        f.seek(0)
        dump(file_data, f, indent = 4)
     