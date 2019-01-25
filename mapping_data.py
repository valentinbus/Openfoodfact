import requests
import pprint
import mysql.connector
import getpass


'''
===========================================================================    
=    Ici nous allons utiliser et populer la db                            =
===========================================================================  
'''

# On définit les inputs user pour qu'il puisse se connecter à sa bdd
# On part du principe que l'utilisateur à déjà sa database mais pas son contenue
# user = str(input('Quel est ton username ?'))
# password = getpass.getpass('MDP?')
# host = str(input('host?'))
# database=str(input('DB?'))

# cnx = mysql.connector.connect(
#     user=user, 
#     password=password, 
#     host=host, 
#     database=database
# )

cnx = mysql.connector.connect(
    user='root', 
    password='root', 
    host='localhost', 
    database='OpenfoodFact'
)
cursor = cnx.cursor()
print('CURSOR---->', cursor)

# === Cela permet d'executer le fichier .sql pour créer les tables dans la bdd (fonctionnel)=== 
def create_db():
    '''
    Lis et éxécute le fichier .sql du dossier pour créer les tables 
    dans la db
    '''
    with open('./create_db.sql', 'r') as file:
        query = file.read()

    print(query)

    cursor.execute(query)
    for row in cursor:
        print(row)



# === Mapping des données ===
create_db()