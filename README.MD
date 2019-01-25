Le projet à pour but de créer et d'utiliser une base de donnée.
Cette base de donnée va être crée et populée par les données fournies par openfoodfact.

Le projet se subdivise en plusieures parties. 


==== create_db.sql ===
Il s'agit de la structure de la base donnée. 
Il sera ensuite appelé par un script python pour être éxécuté en local chez l'utilisateur.

=== collecting_data.py ===
Ce script permet la recupération des données au format json en utilisant l'api d'openfoodfact.
Ces données ont également été mise en local dans le projet dans le cas ou la connexion serait down.

=== mapping_data ===
Ce fichier permet d'établir la connexion entre la base de donnée et les données elles mêmes.
Nous allons utiliser ce script pour populer la db


Prérequis:
    -avoir mysql 
    -créer une bdd du nom de 'Openfoodfact'


Dans la classe CollectData nous avons la classe du même nom qui se découpe de la manière suivante:
    -on lui passe l'url d'openfoodfact 
    -la première méthode va d'établir l'url complet en fonction de la catégorie 
    -la deuxième méthode va parser les éléments de l'url puis récup les données qui nous intéresse pour les 
    tranformer en dictionnaire
    -la troisième méthode va définir la query sql pour insérer dans la dbb

Dans la classe Sql on s'occupe de toute les manipulations sur la bdd:
    -init on passe tous les paramètres d'authent que le user va rentrer 
    -première méthode on utilise ces paramêtres pour pour se connecter à la bdd
    -deuxième méthode on éxécute le fichier sql permettant de créé les tables 
    -troisième méthode on peuple les tables avec les données recup sur OpenfoodFact

