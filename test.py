import mysql.connector
from classes import Sql
# cnx = mysql.connector.connect(
#     user = 'root',
#     password = 'root',
#     host = 'localhost',
#     database = 'Openfoodfact'
# )

# cursor = cnx.cursor()
# cursor.execute("Insert ignore into category (id, name) Values (1, 'pizzas');")
# cnx.commit()
# #cursor.fetchall()
# cursor.close()
# cnx.close()

cnx = mysql.connector.connect(
    user = 'root',
    password = 'root',
    host = 'localhost',
    database = 'Openfoodfact'
)

queries = 'Insert Into product (name, store, link, nutriscore, category_fk) Values ("Pizza Margherita", "Carrefour,Carrefour Bio", "https://fr.openfoodfacts.org/produit/5400101258730/pizza-margherita-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("Pizza 4 fromages bio", "Carrefour", "https://fr.openfoodfacts.org/produit/5400101007802/pizza-4-fromages-bio-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La Pizza Raclette Bacon Fumé", "Carrefour", "https://fr.openfoodfacts.org/produit/3560071120078/la-pizza-raclette-bacon-fume-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La Pizza 4 Fromages", "Carrefour", "https://fr.openfoodfacts.org/produit/3560071083816/la-pizza-4-fromages-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La Pizza Raclette Bacon Fumé", "Carrefour", "https://fr.openfoodfacts.org/produit/3560071083809/la-pizza-raclette-bacon-fume-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La pizza chèvre - lardons fumés", "Carrefour", "https://fr.openfoodfacts.org/produit/3560071083793/la-pizza-chevre-lardons-fumes-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La pizza emmental, jambon, champignons", "Carrefour", "https://fr.openfoodfacts.org/produit/3560071083786/la-pizza-emmental-jambon-champignons-carrefour", "b", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La Pizza 4 Fromages", "Carrefour", "https://fr.openfoodfacts.org/produit/3560070593330/la-pizza-4-fromages-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("Pizza Margherita", "Carrefour", "https://fr.openfoodfacts.org/produit/3560070590780/pizza-margherita-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk)Values ("La Pizza Jambon Fromage", "Carrefour", "https://fr.openfoodfacts.org/produit/3560070555901/la-pizza-jambon-fromage-carrefour", "c", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("3 Pizzas Margherita à la préparation alimentaire au fromage.", "Produits blancs, Carrefour", "https://fr.openfoodfacts.org/produit/3560070348503/3-pizzas-margherita-a-la-preparation-alimentaire-au-fromage-produits-blancs", "c", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("Pizza Especial", "Carrefour", "https://fr.openfoodfacts.org/produit/3560070258604/pizza-pate-fine-speciale-salami-mozzarella-champignon-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("Pizza chorizo", "Carrefour", "https://fr.openfoodfacts.org/produit/3245413824899/pizza-chorizo-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La Pizza Jambon Fromage", "Carrefour,CMI (Carrefour Marchandises Internationales),Groupe Carrefour", "https://fr.openfoodfacts.org/produit/3245412149269/la-pizza-jambon-fromage-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La pizza chèvre - lardons fumés", "Carrefour", "https://fr.openfoodfacts.org/produit/3245412149146/la-pizza-chevre-lardons-fumes-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La pizza emmental, jambon, champignons", "Carrefour", "https://fr.openfoodfacts.org/produit/3245412149085/la-pizza-emmental-jambon-champignons-carrefour", "b", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La pizza jambon fromage", "Carrefour", "https://fr.openfoodfacts.org/produit/3245411955618/la-pizza-jambon-fromage-carrefour", "c", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La Pizza 3 Fromages", "Carrefour,CMI (Carrefour Marchandises Internationales),Groupe Carrefour", "https://fr.openfoodfacts.org/produit/3245411954277/la-pizza-3-fromages-carrefour", "d", "1");Insert Into product (name, store, link, nutriscore, category_fk) Values ("La pizza lardons fumés chèvre", "Carrefour", "https://fr.openfoodfacts.org/produit/3245411955588/la-pizza-lardons-fumes-chevre-carrefour", "d", "1");Insert Into product (name, store, link,nutriscore, category_fk) Values ("Pizza lardons fumes chevre", "Grand Jury, Carrefour", "https://fr.openfoodfacts.org/produit/3245390241160/pizza-lardons-fumes-chevre-grand-jury", "c", "1");'
query = queries.split(';')
print(query)

for qry in query :
    cursor = cnx.cursor()
    cursor.execute(qry)
    cnx.commit()
    cursor.close()



