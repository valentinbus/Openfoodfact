import requests
import pprint



def define_nb_page(count):
    '''
    Fonction permettant de définir le nombre de page à
    parcourrir en fonction du nombre de produit par catégorie 
    Pour l'instant pas d'utilisation mais sera utilse pour bouclé les url 
    en fonction du nomber de page et obtenir tous les produits que l'on veut 
    '''
    nb_per_page = 20 #is always true on openfoodfacts// is number of products per page
    nb_page = 0
    while count >= 0:
        count = count - nb_per_page
        nb_page += 1
    return nb_page



pp = pprint.PrettyPrinter(indent=4)

base_url = 'https://fr.openfoodfacts.org/categorie/pizzas' #this url will change in function of category name 
parameters = {'json' : True}

api_call = requests.get(base_url, params=parameters)
r = api_call.json()

nb_products = r['count']
nb_pages = define_nb_page(nb_products)

def collecting_data():
    for page in range(nb_pages):
        print('PAGE ===> ', page+1)
        url = base_url+'/'+str(page+1)
        print(url)
        api_call2 = requests.get(url, params=parameters)
        r2 = api_call2.json()
        print('R2===>', r2)
        products_list = []

        for i in r2['products']:
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
        return products_list


print(collecting_data())  