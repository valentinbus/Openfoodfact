import pprint
import json

pp = pprint.PrettyPrinter(indent=4)
with open('./pizzas.json', 'r') as file:
    data = file.read()

products_list = []
d = json.loads(data)

for i in d['products']:
    # pp.pprint(type(i))
    # pp.pprint(i['product_name'])
    try:
        product = {
            'NAME': i['product_name'],
            'STORE': i['brands'],
            'LINK': i['url'],
            'NUTRISCORE': i['nutrition_grade_fr'],
            'CATEGORY': 'pizzas'
        }
    except KeyError:
        print("la clé n'a pas été trouvée =================================")
        pass
    products_list.append(product)
    pp.pprint(product)

print(len(products_list))