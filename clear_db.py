import mysql.connector


cnx = mysql.connector.connect(
    user = 'root',
    password = 'root',
    host = 'localhost',
    database = 'Openfoodfact'
)

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
