import json
import re
import mysql.connector
import getpass
from constants import CATEGORY


class Program:
    '''
    Manage all sql interaction with user
    '''

    def __init__(self):
        self.username = None
        self.password = None
        self.host = None
        self.database = 'Openfoodfact'
        self.cnx = None
        self.cat_id = None
        self.nutriscore_product_choose = None

    def get_inf(self):
        '''
        Recup les infos pour la connexion a la db
        '''

        self.username = str(input('Quel est ton username? \n'))
        self.password = getpass.getpass('Quel est ton pass ? \n')
        self.host = 'localhost'


    def connection_db(self):
        '''
        etablie la connexion avec la db
        '''

        try:
            self.cnx = mysql.connector.connect(
                user = self.username,
                password = self.password,
                host = self.host,
                database = self.database
            )
            return True

        except mysql.connector.errors.ProgrammingError :
            print(
                'Le username ou pass est incorrect.\n',
                'Veuillez de nouveau insérer vos identifiants : \n'
            )
            return False

    
    def show_category(self):
        '''
        Show all categories dispnibles for user
        '''
        dict_category = {}

        print('List of categories:\n')
        for i in range(len(CATEGORY)):
            print('{}. {}'.format(i+1, CATEGORY[i]))
            dict_category[i+1] = CATEGORY[i]
        #print(self.dict_category)
        a = True
        while a:
            try:
                self.cat_id = int(input('\n\nChosse id cat : \n'))
                cat_choose = dict_category[self.cat_id]
                a = False
            except ValueError:
                print('It has to be a number')
            except KeyError:
                print('You have to choose a good number for cat')
        
        print('You choose {} category\n\n'.format(cat_choose))
        

    def show_product(self):
        '''
        Show all products of category after the user chooses cat
        '''
        print('Here list of products in this category: \n')
        
        cursor = self.cnx.cursor()
        cursor.execute('select id, name from product where category_fk={};'.format(self.cat_id))
        result = cursor.fetchall()

        for i in range(len(result)):
            print('{}. {}'.format(result[i][0], result[i][1])) #fait matcher l'id des produits avec leurs noms

        a = True
        while a:
            try:
                self.id_product_choose = int(input('\nChoose id product: \n'))
                cursor.execute('select nutriscore from product where id={} and category_fk={};'.format(self.id_product_choose, self.cat_id))
                self.nutriscore_product_choose = cursor.fetchall()[0][0]
                a = False
            except ValueError:
                print('It has to be a number')
            except IndexError:
                print('You have to choose a good number for product')

        cursor.close()
        print('The product you choose have this nutriscore : {} \n\n'.format(self.nutriscore_product_choose))

    def purpose_substitue(self):
        '''
        Purpose substitue product with higher nutriscore
        '''
        cursor = self.cnx.cursor()
        query = (
            'select name, nutriscore from product where nutriscore <= "{}" and category_fk={};'.format(self.nutriscore_product_choose, self.cat_id)
        )
        cursor.execute(query)
        result = cursor.fetchall()

        #affiche le résultat des produits meilleurs ou equivalent
        print('Here the list of product that are better:\n')
        for i in range(len(result)):
            print('{}, nutriscore ===>{}'.format(result[i][0], result[i][1]))
            
        save = input('\nDo you want to save substitue?\n"Y" or "N"\n').upper()
        
        while (save != 'Y') and (save!='N'):
            print('You have to put "Y" or "N"')
            
        if save == 'Y':
            query = ''

