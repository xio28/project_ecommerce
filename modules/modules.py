from json import *
# from clear import *

# clear()


def file_as_list(file):
    with open(file, "r") as f:
        return [loads(x) for x in f.readlines()]


def last_key(dict):
    return 1 if len(dict) == 0 else (list(dict.keys())[-1]) + 1

