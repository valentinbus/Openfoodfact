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

    def get_inf(self):
        self.username = str(input('Quel est ton username? \n'))
        self.password = getpass.getpass('Quel est ton pass ? \n')
        self.host = 'localhost'


    def connection_db(self):
        try:
            self.cnx = mysql.connector.connect(
                user = self.username,
                password = self.password,
                host = self.host,
                database = self.database
            )
            print("Now, you're connected\n\n")
            return True

        except mysql.connector.errors.ProgrammingError :
            print(
                'Le username ou pass est incorrect.\n',
                'Veuillez de nouveau insérer vos identifiants : \n'
            )
            return False


    def test_connection_db(self):
        while prog.connection_db() is False:
            prog.get_inf()
            prog.connection_db()
            print(
                'Le username ou pass est incorrect.\n',
                'Veuillez de nouveau insérer vos identifiants:\n'
            )
        print("Login successfull\n\n")

    
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
                self.cat_id = int(input('Chosse id cat : \n'))
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
        cursor.execute('select name from product where category_fk={};'.format(self.cat_id))
        result = cursor.fetchall()
        for i in range(len(result)):
            print('{}. {}'.format(i+1, result[i][0]))

        a = True
        while a:
            try:
                self.id_product_choose = int(input('Choose id product: \n'))
                cursor.execute('select nutriscore from product where id={} and category_fk={};'.format(self.id_product_choose, self.cat_id))
                nutriscore_product_choose = cursor.fetchall()[0][0]
                a = False
            except ValueError:
                print('It has to be a number')
            except IndexError:
                print('You have to choose a good number for product')

        print('The product you choose have this nutriscore : {}'.format(nutriscore_product_choose))

    def purpose_substitue(self):
        pass
        
        
        

prog = Program()

# prog.get_inf()

while prog.connection_db() is False:
    prog.get_inf()
    prog.connection_db()

prog.show_category()
prog.show_product()

