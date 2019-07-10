import re, sqlite3
global cursor
file = open('C:\\Users\\magshimim\\Desktop\\recipe list.txt',encoding="utf8")
lines = file.readlines()

connection = sqlite3.connect("Recipes.db", check_same_thread=False)
cursor = connection.cursor()

def recipe_name(line):
    if len(line) < 6:
        return False
    if (line[2] is '.' and line[5] is '\t') or (line[2] is '.' and line[4] is '\t') or (line[1] is '.' and line[4] is '\t')or(line[1] is '.' and line[3] is '\t'):
        return True
    return False

def recipe_to_list():
    ing_flag = 0
    dir_flag = 0
    ing = []
    dir = ""
    name = ""
    recipes = []
    for line in lines:
        break_point = line.find('\t')
        if recipe_name(line):
            ing_flag = 0
            dir_flag = 0

            recipes.append((name,ing, dir))
            ing = []
            dir = ""

            name = (line[:break_point], re.compile(r'[\n\r\t]').sub(" ",line[break_point:]).strip())

        elif "Ingredients" in line:
            ing_flag = 1

        elif ing_flag:
            if "Directions" in line:
                ing_flag = 0
                dir_flag = 1
                continue

            if line != '\n':
                ingredient = (line[:break_point], re.compile(r'[\n\t]').sub(" ",line[break_point:]).strip())
                ing.append(ingredient)

        elif dir_flag:
            dir += re.compile(r'[\n\r\t]').sub(" ",line)



    return recipes[1:]

print(recipe_to_list())