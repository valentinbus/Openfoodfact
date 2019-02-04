from classes.init import Init 
from classes.program import Program

def main():
    prog = Program()

    prog.get_inf()

    while prog.connection_db() is False:
        prog.get_inf()
        prog.connection_db()

    prog.show_category()
    prog.show_product()
    prog.purpose_substitue()


init = Init()
arg = init.arg()

if __name__ == "__main__":
    if arg is True:
        arg
    else:
        main()