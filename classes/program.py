"""
Json module to parse data
"""


from classes.sql import Sql
from classes.constants import CATEGORY, CREDENTIALS


class Program:
    """
    Manage all sql interaction with user
    """

    def __init__(self):
        self.cnx = None
        self.cat_id = None
        self.nutriscore_product_choose = None
        self.id_product_choose = None
        self.id_product_substitue = None
        self.response = ['Y', 'N']

    def connection_db(self):
        """
        etablish connection with db
        """
        sql = Sql(
            CREDENTIALS['username'],
            CREDENTIALS['password'],
            CREDENTIALS['host'],
            CREDENTIALS['dbname']
            )

        if sql.connect_db() is False:
            return False

        self.cnx = sql.connect_db()
        return True


    def consult_substitue(self):
        """
        Ask to user if he wants to see his substitues
        """
        while True:
            try:
                response = int(
                    input(
                        "1 - Show your substitues.\n"
                        "2 - What aliment do you want to replace ?\n"
                    ).upper()
                )

                while response not in [1, 2]:
                    print("You have to put 1 or 2")

                break

            except ValueError:
                print("It has to be a number")

        if response == 1:
            query = "SELECT name, nutriscore, store, link  \
                    FROM product \
                    INNER JOIN substitue \
                    ON substitue. id_product_substitue_fk = product.id;"

            cursor = self.cnx.cursor()
            cursor.execute(query)
            results = cursor.fetchall()

            i = 1
            print("\n\nHere list of your substitues :\n--")
            for result in results:
                print(
                    "{}. {} with nutriscore : {}.\n"
                    "Can buy at {} more information on this link : \n{}"
                    .format(
                        i, result[0], result[1], result[2], result[3]
                    )
                )
                i += 1

            print(
                "Ok, now continue!\n\n"
                "Choose a category of product you want to replace"
            )

        else:
            pass

    def show_category(self):
        """
        Show all categories dispnibles for user
        """
        dict_category = {}

        print("List of categories:\n")
        for i, cat in enumerate(CATEGORY):
            print("{}. {}".format(i + 1, cat))
            dict_category[i + 1] = cat

        while True:
            try:
                self.cat_id = int(input("\n\nChoose id cat : \n"))
                cat_choose = dict_category[self.cat_id]
                break
            except ValueError:
                print("It has to be a number")
            except KeyError:
                print("You have to choose a good number for cat")

        print("You choose {} category\n\n".format(cat_choose))

    def show_product(self):
        """
        Show all products of category after the user chooses cat
        """

        print("Here list of products in this category: \n")

        cursor = self.cnx.cursor()
        cursor.execute(
            "SELECT id, name from product WHERE category_fk={};"
            .format(self.cat_id)
        )
        result = cursor.fetchall()

        coef = (self.cat_id-1)*20 #help me to map id with 1 <= id <= 20

        for i in range(len(result)):
            map_id = result[i][0] - coef
            print(
                "{}. {}".format(map_id, result[i][1])
            )  # match id product with their name

        while True:
            try:
                self.id_product_choose = int(input("\nChoose id product: \n"))
                self.id_product_choose = self.id_product_choose + coef
                print(self.id_product_choose)
                cursor.execute(
                    "SELECT nutriscore FROM product \
                    WHERE id={} AND category_fk={};"
                    .format(
                        self.id_product_choose,
                        self.cat_id
                    )
                )
                self.nutriscore_product_choose = cursor.fetchall()[0][0]
                break

            except ValueError:
                print("It has to be a number")
            except IndexError:
                print("You have to choose a good number for product")

        cursor.close()
        print(
            "The product you choose have this nutriscore : {} \n\n"
            .format(
                self.nutriscore_product_choose
            )
        )

    def purpose_substitue(self):
        """
        Purpose substitue product with higher nutriscore
        """
        cursor = self.cnx.cursor()
        query = 'SELECT id, name, nutriscore, store, link \
            FROM product WHERE nutriscore <= "{}" \
            AND category_fk={} AND id != {};'.format(
                self.nutriscore_product_choose,
                self.cat_id,
                self.id_product_choose
            )

        cursor.execute(query)
        result = cursor.fetchall()

        coef = (self.cat_id-1)*20

        # show results of products have better or equivalent nutriscore
        print("Here the list of product that are better or equivalent:\n")
        for i in range(len(result)):
            map_id = result[i][0] - coef
            if result[i][0] is None:
                print('There no substitue')
            else:
                print(
                    "{}. {} with nutriscore : {}. \n"
                    "Can buy at {} more information on this link : \n{}\n"
                    .format(
                        map_id, result[i][1],
                        result[i][2],
                        result[i][3],
                        result[i][4]
                    )
                )

        # define substitue
        while True:
            try:
                self.id_product_substitue = int(input("\nChoose id product: \n"))
                self.id_product_substitue = self.id_product_substitue + coef
                break

            except ValueError:
                print("It has to be a number")
            except IndexError:
                print("You have to choose a good number for product")

        # insert into substitue results
        save = input('\nDo you want to save substitue?\n"Y" or "N"\n').upper()

        while save not in ['Y', 'N']:
            print('You have to put "Y" or "N"')

        if save == "Y":
            query = "INSERT INTO substitue \
            (id_product_to_substitue_fk, id_product_substitue_fk) VALUES ({}, {});".format(
                self.id_product_choose,
                self.id_product_substitue
            )
            cursor.execute(query)
            self.cnx.commit()

        cursor.close()

    def continu(self):
        """
        ask to user if he wants to continu or not
        """

        response = str(input('Do you want to continue ?\n"Y" or "N"\n').upper())
        while response not in self.response:
            print('You have to put "Y" or "N"')

        if response == "Y":
            return True
        return False
