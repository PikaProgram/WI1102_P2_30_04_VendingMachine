# VendingMachineMenu
# Luaran menu vending machine.

# Algoritma
import shutil
import datetime

from reccomendation import get_reccomendation
from util import clean_console


def menu(items):
    # Title Ascii Art Rendering
    clean_console()

    term_dim = shutil.get_terminal_size()

    ascii_art = open("assets/vendtopia.txt", "r")

    print("=" * term_dim.columns, end="")
    print("\n")

    for line in ascii_art.readlines():
        print(" " * ((term_dim.columns - len(line)) // 2), line, end="")

    print("\n")
    print("=" * term_dim.columns)
    print("\n")

    # Render The Available Items And Their Information
    column_size = term_dim.columns // 7
    horizontal_line = "+" + ("-" * column_size + "+") * 5
    horizontal_pad = "|" + (" " * column_size + "|") * 5
    items_table = [horizontal_line]

    for j in range(len(items) // 5):
        items_table += [horizontal_pad]
        for k in range(4):
            table_lines = []
            for i in range(5):
                item_data = items[(i + (j * 5))][k]
                table_lines.append(
                    " " * ((column_size - len(item_data)) // 2 - 1)
                    + item_data
                    + " " * ((column_size - ((column_size - len(item_data)) // 2) - len(item_data)) + 1)
                )
            items_table.append("|" + "|".join(table_lines) + "|")
        items_table += [horizontal_pad, horizontal_line]

    for line in items_table:
        print(" " * ((term_dim.columns - len(line)) // 2), line)

    print("")
    
    print(str(get_reccomendation(datetime.datetime.now().hour)[1]).center(term_dim.columns))    

    print("")
