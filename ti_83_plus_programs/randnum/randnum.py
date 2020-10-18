from random import randint
from ti_83_plus_programs.ti_83_functions.display import clr_home, output
from ti_83_plus_programs.ti_83_functions.get_key import get_key


def lbl_theta():
    while True:
        home = output(1, 1, '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        A = 1
        while A < 50:
            home = output(randint(1, 8), randint(1, 16), str(randint(0, 9)), home)
            B = get_key()
            if B == 'r':
                home = clr_home()
                home = output(1, 1, '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', home)
            if B == 'q':
                _ = clr_home()
                return
            A += 1


if __name__ == '__main__':
    lbl_theta()
