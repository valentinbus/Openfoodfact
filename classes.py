import requests
import pprint
import mysql.connector
from constants import CATEGORY

pp = pprint.PrettyPrinter(indent=4)

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
                #print("la clé n'a pas été trouvée =================================")
                pass
            self.products_list.append(product)
            #pp.pprint(product)
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
        #print('QUERY ----->', query)
        return query


class Sql:
    def __init__(self, user, password, host, databse):
        self.user = str(user)
        self.password = str(password)
        self.host = str(host)
        self.database = str(databse)

    def connect_db(self):
        '''
        Établie la connexion à la db
        '''
        cnx = mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            database = self.database
        )
        return cnx
        
        
    def create_database(self): #category doit être le même argument que pour la fonction create url
        '''
        Lis et éxécute le fichier .sql du dossier pour créer les tables 
        dans la db
        ''' 
        cnx = self.connect_db()     
        cursor = cnx.cursor()

        with open('./create_db.sql', 'r') as file:
            query = file.read()
        
        cursor.execute(query)
        cursor.close()
      
    def map_category(self, category):
        '''
        
        '''
        query = "Insert into category (name) Values ('{}');".format(category)
        cnx = self.connect_db()
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close

        cursor = cnx.cursor()
        cursor.execute("select id from category where name='{}';".format(category))
        result = cursor.fetchall()
        cursor.close()
        category_number = result[0][0]
        return category_number

    def map_data(self, query): #query ici est le retour de fonction CollectData.dict_to_insert_query()
        '''
        Peuple les tables avec les données recup sur openfoodfact
        '''
        query = query.split(';')
        cnx = self.connect_db()
        for qry in query :
            cursor = cnx.cursor()
            cursor.execute(qry)
            cnx.commit()
            cursor.close()



