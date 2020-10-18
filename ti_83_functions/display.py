SCREEN_WIDTH = 18
SCREEN_HEIGHT = 10


def create_display():
    display = [[' ' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]
    column = 1
    while column < SCREEN_WIDTH-1:
        display[0][column] = '-'
        display[SCREEN_HEIGHT-1][column] = '-'
        column += 1
    row = 1
    while row < SCREEN_HEIGHT-1:
        display[row][0] = '|'
        display[row][SCREEN_WIDTH-1] = '|'
        row += 1
    display[0][0] = '+'
    display[0][SCREEN_WIDTH-1] = '+'
    display[SCREEN_HEIGHT-1][0] = '+'
    display[SCREEN_HEIGHT-1][SCREEN_WIDTH-1] = '+'
    return display


def print_display(display):
    for row in display:
        row_string = str(row)
        row_string = row_string.replace('[', '').replace(']', '').replace(',', '').replace('\'', '')
        print(row_string)


def clr_home():
    home = create_display()
    print_display(home)


if __name__ == '__main__':
    clr_home()
