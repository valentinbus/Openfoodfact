import json
import re
import mysql.connector
import getpass
from constants import CATEGORY

# with open('./local/categories.json', 'r') as file:
#         data = file.read()

# dic = json.loads(data)

# list_category_name = []

# for i in range(len(dic['tags'])):
#         list_category_name.append(dic['tags'][i]['name'])



# list_cat_pizza = []

# for i in range(len(list_category_name)):
#         if 'pizzas' in list_category_name[i]:
#                 list_cat_pizza.append(list_category_name[i])

# list_p = []

# for i in range(len(list_cat_pizza)):     
#         list_p.append(re.findall('^en:pizzas', list_cat_pizza[i]))
#         print(list_cat_pizza[i])

# print(list_p)

cnx = mysql.connector.connect(
    user= 'root',
    password= 'root',
    host= 'localhost',
    database= 'Openfoodfact'
)
cursor = cnx.cursor()

cursor.execute('drop table substitue;')
cnx.commit()
cursor.close()
print('table drop')