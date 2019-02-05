import requests

class CollectData:
    '''
    Use to create an url to parse. Then 
     to insert data into sql db
    '''
    def __init__(self, base_url):  #url is 'https://fr.openfoodfacts.org/categorie/'
        self.base_url = str(base_url)
        self.url = None
        self.products_list = []
        self.category_number = None

    def create_url(self, category):
        '''
        Permet d'établir le nouvel url à parser
        en fonction de la catégorie
        '''
        print("generate url")
        self.url = self.base_url + str(category)
        print("Url {} is created".format(self.url))
        return category #on le retourne pour pouvoir le placer en argument dans la fonction create_databse

    def json_to_dict(self, category_number): # Définir le paramêtre catégorie 
        '''
        Convert reponse of url parse to dict
        '''
        self.category_number = category_number
        parameters = {'json' : True}
        api_call = requests.get(self.url, params=parameters)
        r = api_call.json()

        for i in r['products']:
            try:
                product = {
                    'name': i['product_name'],
                    'store': i['brands'],
                    'link': i['url'],
                    'nutriscore': i['nutrition_grade_fr'],
                    'category_fk': self.category_number
                }
            except KeyError:
                pass
            self.products_list.append(product)
            self.products_list

    def dict_to_insert_query(self): 
        '''
        Convert dict to query
        '''  
        query = ''
        for product in self.products_list:
            a = [f'"{x}"' for x in product.values()] #f pour .format 
            qry = "Insert Into product (%s) Values (%s);" % (', '.join(product.keys()), ', '.join(a))
            query+=qry
        return query