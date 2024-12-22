import os


def clean_console():
    os.system('cls' if os.name == 'nt' else 'clear')
