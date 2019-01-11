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

