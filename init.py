import mysql.connector
from classes import Sql, CollectData
from constants import CATEGORY


def init_db():

    sql = Sql('root', 'root', 'localhost', 'Openfoodfact') #tous les paramêtres pour établir la connexion
    cnx = sql.connect_db()
    
    cursor = cnx.cursor()

    try:
        cursor.execute('drop table substitue;')
        cnx.commit()
        cursor.close()

        cursor = cnx.cursor()
        cursor.execute('drop table product;')
        cnx.commit()
        cursor.close()

        cursor = cnx.cursor()
        cursor.execute('drop table category;')
        cnx.commit()
        cursor.close()
    except mysql.connector.errors.ProgrammingError as err:
        print('La base de donnée est déjà clean')


    sql.create_database() #initialise les tables de la db


    ###MAP DATA###

    for i in range(len(CATEGORY)):
        cat_number = sql.map_category(CATEGORY[i]) #insert la catégorie et retourne l'id de la catégorie

        init_collect_data = CollectData('https://fr.openfoodfacts.org/categorie/') #initialise le lien générique qui sera modifié en fonction des catégories 


        init_collect_data.create_url(CATEGORY[i]) #crée l'url de la catégorie en question
        init_collect_data.json_to_dict(cat_number) #crée le dict qui sera insérer dans la table product et insére la foreign key a savoir l'id de la catégorie de la table category
        query = init_collect_data.dict_to_insert_query() #crée la query pour insérer les datas 
        sql.map_data(query)


print('JE SUIS UN CHAMPION !!!!')

if __name__ == "__main__":
    print('JE SUIS dans le main !!!!')
    init_db()

