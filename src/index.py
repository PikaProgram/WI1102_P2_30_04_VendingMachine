# VendingMachine

# Algoritma
from handler import handler
from menu import menu

# Import The Drinks Data
items_raw_data = open("data/items.csv", "r")
items_data = []

for line in items_raw_data.readlines():
    items_data_list = line.strip().split(",")
    items_data.append(items_data_list)

items_raw_data.close()

menu(items_data)
handler(items_data)
