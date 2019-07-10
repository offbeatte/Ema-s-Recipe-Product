import re, sqlite3, os
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

recipes = recipe_to_list()


if not os.path.isfile("Recipes.db"):
    create_db_command = "CREATE TABLE recipes( id CHAR(5) PRIMARY KEY, name CHAR(50), directions CHAR(8000));"
    cursor.execute(create_db_command)
    create_db_command = "CREATE TABLE ingredients( ingredient CHAR(50) PRIMARY KEY);" #is there even any need for this?
    cursor.execute(create_db_command)
    create_db_command = "CREATE TABLE connection ( recipe_id CHAR(5), ingredient CHAR(50), quantity CHAR(50)," \
                        "FOREIGN KEY(recipe_id) REFERENCES recipes(id) FOREIGN KEY(ingredient) REFERENCES ingredients(ingredient));"
    cursor.execute(create_db_command)
    create_db_command = "CREATE TABLE users ( username CHAR(50) PRIMARY KEY, password CHAR(50));"
    cursor.execute(create_db_command)


#adding all the data into the db:
#for recipe in recipes:
#    command = 'INSERT INTO recipes ("{}","{}","{}")'.format(recipe[0][0],recipe[0][1],recipe[2])











