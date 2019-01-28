import mysql.connector


cnx = mysql.connector.connect(
    user = 'root',
    password = 'root',
    host = 'localhost',
    database = 'Openfoodfact'
)

def query1():
    cursor = cnx.cursor()
    cursor.execute('drop table substitue;')
    cnx.commit()
    cursor.close()

def query2():
    cursor = cnx.cursor()
    cursor.execute('drop table product;')
    cnx.commit()
    cursor.close()

def query3():
    cursor = cnx.cursor()
    cursor.execute('drop table category;')
    cnx.commit()
    cursor.close()



query1()
query2()
query3()


