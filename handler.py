# VendingMachineInputHandler
# Logika transaksi vending machine.

# Algoritma

import time

from menu import menu

def handler(itemsData):
  # Masukan Kode Pengguna
  itemCode = str(input("Masukan Kode Item Yang Mau Dibeli: ")).upper()
  itemData = []
  validCode = False
  
  # Menterminasi program jika diberi input "Q"
  if itemCode == "Q":
    exit()
  
  # Memvalidasi kode masukan pengguna dengan database
  for item in itemsData:
    if item[3] == itemCode:
      validCode = True
      itemData = item

  # Logika bila kode masukan valid
  if validCode:
    itemName, itemStock, itemPrice, itemCode = itemData
    itemStock = int(itemStock)
    # Pengecekan stok
    if itemStock == 0:
      print("Stok Item Habis, Silahkan Memilih Kode Item Yang Lain")
      time.sleep(3)
      menu(itemsData)
      handler(itemsData)
    else:
      paymentMethod = input(f"Anda Akan Membeli {itemName} Dengan Harga {itemPrice}, Pilih Metode Pembayaran (q)ris/(t)unai/(b)atal: ")
      payment(paymentMethod, itemsData, itemData)
  # Logika bila kode masukan tidak valid
  else:
    print("Kode Yang Diberikan Tidak Valid, Silahkan Memasukan Salah Satu Kode Item Yang Tertera")
    handler(itemsData)

# Logika pembayaran
def payment(paymentMethod, itemsData, itemData):
  successfulTransaction = False
  # Jika input "b", kembali ke menu
  if paymentMethod == "b":
    menu(itemsData)
    handler(itemsData)
  # Jika input "q", pembayaran menggunakan qris
  elif paymentMethod == "q":
    qr = [
      "▄▄▄▄▄▄▄  ▄ ▄▄ ▄▄ ▄ ▄▄ ▄▄▄ ▄▄▄▄▄▄▄",
      "█ ▄▄▄ █ ▀█▄█▀ ▀▄█▀  ▀▀▄ ▄ █ ▄▄▄ █",
      "█ ███ █  ▄ █▄█  ▄▄▄▄▀  ▀█ █ ███ █",
      "█▄▄▄▄▄█ █ █ █▀▄ ▄ █ ▄▀▄ ▄ █▄▄▄▄▄█",
      "▄▄▄▄▀▀▄▄  ▀ ▄▀▀██  ▀  ▄▄   ▄     ",
      "▄▀▀▀█▄▀ ▄▀  ▀▀ ▀█▄▀ ▀▀█▄█▀▀ ▄█▄▄ ",
      "██ ▀▄▀▄██▀█▀██ ▀  ▀▀█ █ ▀▀█▄▀▄▀▄█",
      "▄ ▀▄▄▀▄▄▀▄▀▄█ ▀█ ▄▄█  ▄▄▄▄▀ ▄▀▀█▀",
      "██ ▀ ▄▄▄▄█▀█   ▄▄█▀▀▄▄  █▀█▄▀▀█▄▀",
      "▄▀  █▀▄▀▄█▄ ▀█ ██▄▀▄█  ▄█   ▄ ▀▄ ",
      "█▄  █▄▀█▄ ▄▀▀▀▀▀ ▀ ▀█▀ █▄▄▄█ █ █ ",
      "▀ █   ▄▄▀█▄█ ▄█ ▀█ ▀ ▄   █▀█▀▀█▄▀",
      "▄▄▀█▀▄▄█▀█ █▀▀▀▄▄▀ ▄ █▄▄███▄███ █",
      "▄▄▄▄▄▄▄ █  ▀█▀▄ ███▄█▄█▄█ ▄ ███▄▄",
      "█ ▄▄▄ █ █▀▀█▀█▀▀ ▀▀▀▀▀  █▄▄▄█ ▄▄█",
      "█ ███ █  █  ▄ █▀▀ ▀▀▄▄██  ▀▄ ██ ▀",
      "█▄▄▄▄▄█  ▀▄▀▄▄▄█ █▀ █ ▀█▄▀ █ █ ▀█"
    ]
    # Luaran Kode QR
    for line in qr:
      print(line)
    # Validasi pembayaran
    successfulTransaction = True if input("Silahkan Bayar Menggunakan QR Di Atas (y)a/(t)idak): ").lower() == "y" else False
  # Jika input "t", pembayaran menggunakan tunai
  elif paymentMethod == "t":
    balanceOwed = int(itemData[2].replace(".",""))
    balancePaid = 0
    # Logika transaksi tunai
    while balanceOwed > balancePaid:
      cashInput = input("Silahkan Masukan Uang Tunai (5/10/20/50/75/100/(b)atal): ")
      if cashInput == "b":
        payment("b", itemsData, itemData)
      elif (cashInput in ["5","10","20","50","75","100"]):
        balancePaid += int(cashInput)*1000
      successfulTransaction = True
  else:
    payment("q", itemsData, itemData)

  # Validasi kesuksesan transaksi
  if successfulTransaction:
    updatedItemsData = []
    for item in itemsData: 
      if item[0] != itemData[0]:
        updatedItemsData.append(item)
      else:
        item[1] = str(int(item[1]) - 1)
        updatedItemsData.append(item)
    print("Terima Kasih Sudah Bertransaksi, Selamat Menikmati!")
    time.sleep(3)
    menu(updatedItemsData)
    handler(updatedItemsData)
    lines = []
    for item in updatedItemsData:
      lines.append(",".join(item))
    itemFile = open("./items.csv", "rw")
    itemFile.write("\n".join(lines))
    itemFile.close()
  else:
    print("Transaksi Gagal, Silahkan Memesan Item Lagi")
    time.sleep(3)
    menu(itemsData)
    handler(itemsData)
