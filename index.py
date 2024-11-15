# VendingMachine

# Kamus
#

# Algoritma

# Print Items and their Information (Name, Stock, Price, Etc.)
# Business Logic

from handler import handler
from menu import menu

# Import The Drinks Data
itemsRawData = open("./items.csv", "r")
itemsData = []

for line in itemsRawData.readlines():
  itemsDataList = line.strip().split(",")
  itemsData.append(itemsDataList)

itemsRawData.close()

menu(itemsData)
handler(itemsData)