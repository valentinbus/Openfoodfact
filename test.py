import mysql.connector





class Db:
    def __init__(self):
        pass

    def connect_db(self):
        cnx = mysql.connector.connect(
            user = 'root',
            password = 'root',
            host = 'localhost',
            database = 'Openfoodfact'
        )
        return cnx

    def db(self):
        cnx = self.connect_db()
        print(cnx)
        cnx.cursor().e






db = Db()
db.db()

