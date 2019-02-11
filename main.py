'''
required classes
'''

from classes import Init
from classes import Program


def main():
    '''
    all program
    '''

    prog = Program()

    connect = prog.connection_db()

    if connect is False:
        print(
            "You have to put good credentials "
            "in ./classes/constants.py CREDENTIALS"
        )
    else:
        run = True
        while run:
            prog.consult_substitue()
            prog.show_category()
            prog.show_product()
            prog.purpose_substitue()

            run = prog.continu()


ARG = None

try:
    INIT_DB = Init()
    ARG = INIT_DB.arg()
except AttributeError:
    pass


if __name__ == "__main__":
    if ARG is True:
        ARG
    else:
        main()
