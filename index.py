# VendingMachine

# Kamus
#

# Algoritma

# Print Items and their Information (Name, Stock, Price, Etc.)
# Business Logic

import os
import shutil

# Title Ascii Art Rendering
os.system('cls' if os.name == 'nt' else 'clear')

termDim = shutil.get_terminal_size()

asciiArt = open("./vendtopia.txt", "r")

print("="*termDim.columns)
print("\n"*2)

for line in asciiArt.readlines():
  print(" "*((termDim.columns-len(line))//2), line, end="")

print("\n"*2)
print("="*termDim.columns)
print("\n"*2)

# Import The Drinks Data
itemsRawData = open("./drinks.csv", "r")
itemsData = {}

for line in itemsRawData.readlines():
  itemsDataList = line.strip().split(",")
  itemsData[itemsDataList[0].replace(" ","").lower()] = itemsDataList

# itemsTable = [
#   "+"+("-"*25+"+")*5
# ]

# print(str.join("\n",itemsTable))