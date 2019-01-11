import requests
import pprint

''' 
===========================================================================    
=    Toute cette partie sert à :                                          =  
=    Recup la data.json via l'api                                         =
=    Le but est ensuite de peupler la bdd avec ses données là             =
=    Pour ce projet nous allons utiliser les données de manière locale    =
=    c'est pourquoi cette partie reste en commentaire.                    =
=    Elle correspond à l'utilisation de l'api                             =
===========================================================================   
'''

def define_nb_page(count):
    '''
    Fonction permettant de définir le nombre de page à
    parcourrir en fonction du nombre de produit par catégorie 
    Pour l'instant pas d'utilisation mais sera utilse pour bouclé les url 
    en fonction du nomber de page et obtenir tous les produits que l'on veut 
    '''
    nb_per_page = 20 #is always true on openfoodfacts// is number of products per page
    nb_page = 1
    while count >= 0:
        count = count - nb_per_page
        nb_page += 1
    return nb_page

'''
================================
=   Définition des variables   =
================================ 
'''

pp = pprint.PrettyPrinter(indent=4)
base_url = 'https://fr.openfoodfacts.org/categorie/pizzas' #this url will change in function of category name 
parameters = {'json' : True}
api_call = requests.get(base_url, params=parameters)
r = api_call.json()
nb_products = r['count']
nb_pages = define_nb_page(nb_products)

for page in range(nb_pages):
    print('PAGE ===> ', page)
    url = base_url+'/'+str(page)
    print(url)
    

'''
============================================================================   
==    Ici on créé les produits avec leurs caractéristiques                ==
==    On les ajoute à une liste qui nous permettra de mapp les datas      ==
============================================================================   
'''

def json_to_dict_pizza(): # Définir le paramêtre catégorie 
    products_list = []
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
        products_list.append(product)
        pp.pprint(product)
    return products_list

    print(len(products_list))

def dict_to_insert_query(products_list):   
    for product in products_list:
        qmarks = ', '.join('?' * len(product))
        a = [f'"{x}"' for x in product.values()] #f pour .format 
        qry = "Insert Into PRODUCT (%s) Values (%s);" % (', '.join(product.keys()), ', '.join(a))
        print(qry)

products_list = json_to_dict_pizza()

# with open('./writing-data.sql', 'w') as f:
#     f.write(str(dict_to_query(products_list)))

dict_to_insert_query(products_list)

