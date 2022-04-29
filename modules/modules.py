from json import *


<<<<<<< HEAD

def file_as_list(file):
    with open(file, "r") as f:
        return [loads(x) for x in f.readlines()]
=======
def file_as_list(filename):
    with open(filename, "r") as f:
        return [loads(x) for x in f.readlines()]

>>>>>>> d7bdc8dd6f08a2f90086fbd98738fda5a5a122dc

def last_key(dict):
    return 1 if len(dict) == 0 else (list(dict)[-1]) + 1

<<<<<<< HEAD
def last_key(dict):
    return 1 if len(dict) == 0 else (list(dict.keys())[-1]) + 1
=======
>>>>>>> d7bdc8dd6f08a2f90086fbd98738fda5a5a122dc

def write_json(new_data, filename):
    file_data = file_as_list(filename)

    with open(filename, 'a') as f:
        f.write(dumps(new_data) + '\n')

# def user_exists(username, filename):
#     file_data = file_as_list(filename)
#     print(file_data)
    # for data in file:
    #     print(data)

def anadir_ingrediente(n_recipe, n_ingredient):

    recipe_file = file_to_list("recetas_v1.txt")

    with open("aux_recipe.txt", "w") as f:

        for recipe in recipe_file:
            if recipe["nombre"] == n_recipe and n_ingredient not in recipe["ingredientes"]:
                recipe["ingredientes"].append(n_ingredient)

            f.write(json.dumps(recipe) + "\n")

        rename_file("aux_recipe.txt", "recetas_v1.txt")
