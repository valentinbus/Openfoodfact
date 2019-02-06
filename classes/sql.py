import mysql.connector


class Sql:
    '''
    This class manages all interactions with db sql 
    '''

    def __init__(self, user, password, host, databse):
        self.user = str(user)
        self.password = str(password)
        self.host = str(host)
        self.database = str(databse)

    def connect_db(self):
        '''
        Established connection to the db
        '''
        cnx = mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            database = self.database
        )
        return cnx
        
        
    def create_database(self): #category has to be same argument to create url function
        '''
        Read and execute the .sql file in the folder to create the tables
        in the db
        ''' 
        cnx = self.connect_db()     
        cursor = cnx.cursor()

        with open('./sql/create_db.sql', 'r') as file:
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

    def map_data(self, query): #here query is the return of dict_to_insert_query function
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