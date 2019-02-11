"""
Module uses to use http verb
"""

import requests


class CollectData:
    """
    Use to create an url to parse. Then
    to insert data into sql db
    """

    def __init__(self, base_url):  # url is 'https://fr.openfoodfacts.org/categorie/'
        self.base_url = str(base_url)
        self.url = None
        self.products_list = []
        self.category_number = None

    def create_url(self, category):
        """
        create new url to parse with category in paramter
        """
        print("generate url")
        self.url = self.base_url + str(category)
        print("Url {} is created".format(self.url))
        return category  # return to put him in paramter of function create_databse

    def json_to_dict(self, category_number):  # define parameter category
        """
        Convert reponse of url parse to dict
        """
        self.category_number = category_number
        parameters = {"json": True}
        api_call = requests.get(self.url, params=parameters)
        req = api_call.json()

        for i in req["products"]:
            try:
                product = {
                    "name": i["product_name"],
                    "store": i["brands"],
                    "link": i["url"],
                    "nutriscore": i["nutrition_grade_fr"],
                    "category_fk": self.category_number,
                }
            except KeyError:
                pass
            self.products_list.append(product)

    def dict_to_insert_query(self):
        """
        Convert dict to query
        """
        query = ""
        for product in self.products_list:
            add = [f'"{x}"' for x in product.values()]  # f for .format
            qry = "Insert Into product (%s) Values (%s);" % (
                ", ".join(product.keys()),
                ", ".join(add),
            )
            query += qry
        return query
