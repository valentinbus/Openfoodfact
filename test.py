import json
import re
import mysql.connector
import getpass
from classes import CATEGORY

with open('./local/categories.json', 'r') as file:
        data = file.read()

dic = json.loads(data)

list_category_name = []

for i in range(len(dic['tags'])):
        list_category_name.append(dic['tags'][i]['name'])



print(list_category_name)

# with open('./local/cat.py', 'w') as file:
#     file.write(str(list_category_name))
# # list_cat_pizza = []

# # for i in range(len(list_category_name)):
# #         print(list_category_name[i])
                
list_cat = []

for cat in list_category_name:
    cat = cat.lower()
    cat = cat.replace(' ', '-')
    cat = cat.replace('é', 'e')
    cat = cat.replace('è', 'e')
    cat = cat.replace('à', 'a')
    list_cat.append(cat)

print(list_cat)

with open('./local/cat.py', 'w') as file:
    file.write(str(list_cat))