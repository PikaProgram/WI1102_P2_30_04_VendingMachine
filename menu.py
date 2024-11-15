import shutil

from util import cleanConsole

def menu(items):
  # Title Ascii Art Rendering
  cleanConsole()

  termDim = shutil.get_terminal_size()

  asciiArt = open("./vendtopia.txt", "r")

  print("="*termDim.columns, end="")
  print("\n")

  for line in asciiArt.readlines():
    print(" "*((termDim.columns-len(line))//2), line, end="")

  print("\n")
  print("="*termDim.columns)
  print("\n")

  # Render The Available Items And Their Information
  columnSize = termDim.columns//7
  horizontalLine = "+"+("-"*(columnSize)+"+")*5
  horizontalPad = "|"+(" "*(columnSize)+"|")*5
  itemsTable = [horizontalLine]
  
  tableLines = []
  for j in range(len(items)//5):
    itemsTable += [horizontalPad]
    for k in range(4):
      tableLines = []
      for i in range(5):
        itemData = items[(i+(j*5))][k]
        tableLines.append(
            " "*((columnSize-len(itemData))//2-1)
          + itemData
          + " "*((columnSize-((columnSize-len(itemData))//2) - len(itemData))+1)
          )
      itemsTable.append("|"+"|".join(tableLines)+"|")
    itemsTable += [horizontalPad, horizontalLine]


  for line in itemsTable:
    print(" "*((termDim.columns-len(line))//2), line)
  
  print("")
