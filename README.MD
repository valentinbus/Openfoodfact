
  

*The project aims to create and use a database.

The user can choose a food product that is part of the openfoodfact database.

Once a product chooses the program will propose a list of food having a superior nutriscore or equivalent.*

  

  

## **Prerequisites:**

  

- have mysql

- create a db named 'Openfoodfact'

  
  

  
  

  

  

## Operations:

  

**Folder classes:**

  

- collect_data.py:

- we pass him the url of openfoodfact

- the first method will establish the full url according to the category

- the second method will parse the elements of the url then recover the data which interests us for the translate into dictionary

- the third method will define the query sql to insert in the db

- sql:

- init we pass all the parameters of authenticity that the user will enter

- first method we use these parameters to connect to the database

- second method we execute the file sql allowing to create the tables

- third method we populate tables with data collected on OpenfoodFact

- init_db.py:

- allows to clear the tables by dropping them

- use collect_data to populate datas in tables

- program:

- generate all the run part of the program

- request if the user wants to consult the products he has already selected

- request if the product category that the user wants to know

- main: main program

  

## How to use it:

  
  

  

For a first use it is necessary to do:

  
  

- Change CREDENTIALS in constants file.

Then execute the following command:

  

python3 main.py --init

  

After that you can run the progam:

  

python3 main.py

  


  


##

  

Once the connection is established the user will have to choose between:

  

Consult the substitutions he has already seen (empty if it's the first time)

  

Or choose a product category for which he will have to choose a particular product

  

Then he will be able to record or not the substitute of his choice
