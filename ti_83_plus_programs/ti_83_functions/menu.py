from ti_83_plus_programs.ti_83_functions.get_key import get_key


def create_menu(menu_items):
    print(menu_items[0])
    menu_index = 1
    menu_item = 1
    while menu_index < len(menu_items):
        print('{}: {}'.format(menu_item, menu_items[menu_index]))
        menu_index += 2
        menu_item += 1


def menu(menu_items):
    create_menu(menu_items)
    user_input = get_key()


if __name__ == '__main__':
    test_list = ('BIOS', 'RAM', 1, 'ARC', 2, 'CD/DVD DRIVE', 3)
    menu(test_list)
