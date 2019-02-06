from classes import Init 
from classes import Program


def main():
    prog = Program()

    prog.get_inf()

    a = True
    while a:
        while prog.connection_db() is False:
            prog.get_inf()
            prog.connection_db()
        print("Now you're connected\n\n")
        
        prog.consult_substitue()
        prog.show_category()
        prog.show_product()
        prog.purpose_substitue()

        a = prog.continu()


init_db = Init()
arg = init_db.arg()

if __name__ == "__main__":
    if arg is True:
        arg
    else:
        main()