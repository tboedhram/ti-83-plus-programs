import os
import platform
OS = platform.system()
if OS == 'Windows':
    import msvcrt as get_keyboard_input
else:
    import getch as get_keyboard_input


def get_key():
    if OS == 'Windows':
        user_input = str(get_keyboard_input.getch())
        user_input = user_input.replace('b', '').replace('\'', '')
        return user_input
    else:
        return str(get_keyboard_input.getch())


def clear():
    if OS == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    return
