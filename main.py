from classes import Init 
from classes import Program


def main():
    prog = Program()

    connect = prog.connection_db()

    if connect is False:
        print('You have to put good credentials in ./classes/constants.py CREDENTIALS')
    else:
        a = True
        while a:
            
            prog.consult_substitue()
            prog.show_category()
            prog.show_product()
            prog.purpose_substitue()

            a = prog.continu()


arg = None

try:
    init_db = Init()
    arg = init_db.arg()
except AttributeError:
    pass


if __name__ == "__main__":
    if arg is True:
        arg
    else:
        main()