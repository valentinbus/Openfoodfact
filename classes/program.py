import json
import re
import mysql.connector
import getpass
from classes.constants import CATEGORY

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
        self.id_product_choose = None
        self.id_product_substitue = None

    def get_inf(self):
        '''
        Recup les infos pour la connexion a la db
        '''

        self.username = str(input('What is your username ? \n'))
        self.password = getpass.getpass('What is your password ? \n')
        self.host = 'localhost'


    def connection_db(self):
        '''
        etablish connection with db
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
                'Username or pass is incorrect.\n',
                'Please retry to login : \n'
            )
            return False


    def consult_substitue(self):
        '''
        Ask to user if he wants to see his substitues
        '''

        a = True
        while a:
            try:
                response = int(input(
                '1 - Show your substitues.\n2 - What aliment do you want to replace ?\n'
                ).upper())

                while (response!=2) and (response!=1):
                    print('You have to put 1 or 2')
                
                a = False

            except ValueError:
                print('It has to be a number')

        if response == 1:
            query = 'SELECT name, nutriscore, store, link  FROM product INNER JOIN substitue on substitue. id_product_substitue_fk = product.id;'

            cursor = self.cnx.cursor()
            cursor.execute(query)
            results = cursor.fetchall()

            i = 1
            print('\n\nHere list of your substitues :\n--')
            for result in results:
                print('{}. {} with nutriscore : {}. Can buy at {} more information on this link : {}'.format(i, result[0], result[1], result[2], result[3]))
                i+=1

            print('Ok, now continue!\n')
            
        else:
            pass

    def show_category(self):
        '''
        Show all categories dispnibles for user
        '''
        dict_category = {}

        print('List of categories:\n')
        for i in range(len(CATEGORY)):
            print('{}. {}'.format(i+1, CATEGORY[i]))
            dict_category[i+1] = CATEGORY[i]

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
            print('{}. {}'.format(result[i][0], result[i][1])) #match id product with their name

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
            'select id, name, nutriscore, store, link from product where nutriscore <= "{}" and category_fk={};'.format(self.nutriscore_product_choose, self.cat_id)
        )
        cursor.execute(query)
        result = cursor.fetchall()

        #show results of products have better or equivalent nutriscore
        print('Here the list of product that are better or equivalent:\n')
        for i in range(len(result)):
            print('{}. {} with nutriscore : {}. Can buy at {} more information on this link : {}'.format(result[i][0], result[i][1], result[i][2], result[i][3], result[i][4]))

        #define substitue
        a = True
        while a:
            try:
                self.id_product_substitue = int(input('\nChoose id product: \n'))
                a = False
            except ValueError:
                print('It has to be a number')
            except IndexError:
                print('You have to choose a good number for product')


        #insert into substitue results
        save = input('\nDo you want to save substitue?\n"Y" or "N"\n').upper()
        
        while (save != 'Y') and (save!='N'):
            print('You have to put "Y" or "N"')

        if save == 'Y':
            query = 'INSERT INTO substitue (id_product_to_substitue_fk, id_product_substitue_fk) VALUES ({}, {});'.format(self.id_product_choose, self.id_product_substitue)
            cursor.execute(query)
            self.cnx.commit()

        cursor.close()

    def continu(self):
        response = str(input('Do you want to continue ?\n"Y" or "N"\n').upper())
        while (response!='Y') and (response!='N'):
            print('You have to put "Y" or "N"')

        if response == 'Y':
            return True
        else:
            return False