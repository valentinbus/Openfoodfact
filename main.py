from classes import Init 
from classes import Program


def main():
    prog = Program()

    prog.get_inf()

    while prog.connection_db() is False:
        prog.get_inf()
        prog.connection_db()
    print("Now you're connected\n\n")

    prog.show_category()
    prog.show_product()
    prog.purpose_substitue()


init_db = Init()
arg = init_db.arg()

if __name__ == "__main__":
    if arg is True:
        arg
    else:
        main()