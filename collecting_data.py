import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Collecting_data:
    def __init__(self, base_url):  #url is 'https://fr.openfoodfacts.org/categorie/'
        self.base_url = str(base_url)

    def create_url(self, category):
        '''Permet d'établir le nouvel url à parser
        en fonction de la catégorie'''
        self.url = self.base_url + str(category)

    def json_to_dict_pizza(self): # Définir le paramêtre catégorie 
        parameters = {'json' : True}
        api_call = requests.get(self.url, params=parameters)
        r = api_call.json()

        self.products_list = []
        for i in r['products']:
            # pp.pprint(type(i))
            # pp.pprint(i['product_name'])
            try:
                product = {
                    'NAME': i['product_name'],
                    'STORE': i['brands'],
                    'LINK': i['url'],
                    'NUTRISCORE': i['nutrition_grade_fr'],
                    'CATEGORY_FK': 1
                }
            except KeyError:
                print("la clé n'a pas été trouvée =================================")
                pass
            self.products_list.append(product)
            pp.pprint(product)
            self.products_list

    def dict_to_insert_query(self):   
        for product in self.products_list:
            qmarks = ', '.join('?' * len(product))
            a = [f'"{x}"' for x in product.values()] #f pour .format 
            query = "Insert Into PRODUCT (%s) Values (%s);" % (', '.join(product.keys()), ', '.join(a))
            query+=query
        print(query)




############################
#########TEST###############
############################     
       
collect_pizza = Collecting_data('https://fr.openfoodfacts.org/categorie/')
collect_pizza.create_url('pizza')
print(collect_pizza.url)
print(collect_pizza.json_to_dict_pizza())
print(collect_pizza.dict_to_insert_query())
