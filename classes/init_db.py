import argparse
import mysql.connector
from classes.collect_data import CollectData
from classes.sql import Sql
from classes.constants import CATEGORY, CREDENTIALS



class Init:
    def __init__(self):
        pass

    def init_db(self):

        sql = Sql(CREDENTIALS['username'], CREDENTIALS['password'], CREDENTIALS['host'], CREDENTIALS['dbname']) #all parameters to etablish connection
        cnx = sql.connect_db()
        cursor = cnx.cursor()
        try:
            cursor.execute('drop table substitue;')
            cnx.commit()
            cursor.close()
        except mysql.connector.errors.ProgrammingError:
            print('La table substitue de donnée est déjà clean')

        try:
            cursor = cnx.cursor()
            cursor.execute('drop table product;')
            cnx.commit()
            cursor.close()
        except mysql.connector.errors.ProgrammingError:
            print('La table product de donnée est déjà clean')

        try:
            cursor = cnx.cursor()
            cursor.execute('drop table category;')
            cnx.commit()
            cursor.close()
        except mysql.connector.errors.ProgrammingError:
            print('La table category de donnée est déjà clean')
        


        sql.create_database() #initialise table in db


        ###MAP DATA###

        for i in range(len(CATEGORY)):
            cat_number = sql.map_category(CATEGORY[i]) #insert category and return the id of category

            init_collect_data = CollectData('https://fr.openfoodfacts.org/categorie/') #initialise generic lien that will be modify in function of category


            init_collect_data.create_url(CATEGORY[i]) #create url of category 
            init_collect_data.json_to_dict(cat_number) #create dictionary that will be insert in product table and insert foreign key (id of category)
            query = init_collect_data.dict_to_insert_query() #create query to insert data
            sql.map_data(query)

    def arg(self):
            parser = argparse.ArgumentParser()
            parser.add_argument('--init', '-i', action = 'store_true', help='initalise the db')
            args = parser.parse_args()

            if args.init:
                self.init_db()
                return True