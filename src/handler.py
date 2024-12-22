# VendingMachineInputHandler
# Logika transaksi vending machine.

# Algoritma

import datetime
import time

from menu import menu
from payment import payment
from reccomendation import get_reccomendation

def handler(items_data):
    # Masukan Kode Pengguna
    item_code = str(input("Masukan Kode Item Yang Mau Dibeli kode/(r)ekomendasi: ")).upper()
    item_data = []
    valid_code = False

    # Menterminasi program jika diberi input "Q"
    if item_code == "Q":
        exit()

    if item_code == "R":
        reccomendation_code = get_reccomendation(datetime.datetime.now().hour)[0]
        for item in items_data:
            if item[3] == reccomendation_code:
                valid_code = True
                item_data = item
                break

    # Memvalidasi kode masukan pengguna dengan database
    for item in items_data:
        if item[3] == item_code:
            valid_code = True
            item_data = item
            break

    # Logika bila kode masukan valid
    if valid_code:
        item_name, item_stock, item_price, item_code = item_data
        item_stock = int(item_stock)
        # Pengecekan stok
        if item_stock == 0:
            print("Stok Item Habis, Silahkan Memilih Kode Item Yang Lain")
            time.sleep(3)
            menu(items_data)
            handler(items_data)
        else:
            payment_method = input(
                f"Anda Akan Membeli {item_name} Dengan Harga {item_price}, Pilih Metode Pembayaran (q)ris/(t)unai/(b)atal: ")
    # Logika bila kode masukan tidak valid
    else:
        print("Kode Yang Diberikan Tidak Valid, Silahkan Memasukan Salah Satu Kode Item Yang Tertera")
        handler(items_data)

    # Jika input "b", kembali ke menu
    if payment_method == "b":
        menu(items_data)
        handler(items_data)
    else:
        successful_transaction = payment(payment_method, items_data, item_data)

    # Validasi kesuksesan transaksi
    if successful_transaction:
        updated_items_data = []
        for item in items_data:
            if item[0] != item_data[0]:
                updated_items_data.append(item)
            else:
                item[1] = str(int(item[1]) - 1)
                updated_items_data.append(item)
        print("Terima Kasih Sudah Bertransaksi, Selamat Menikmati!")
        time.sleep(3)
        lines = []
        for item in updated_items_data:
            lines.append(",".join(item))
        item_file = open("data/items.csv", "w")
        item_file.write("\n".join(lines))
        item_file.close()
        menu(updated_items_data)
        handler(updated_items_data)
    else:
        print("Transaksi Gagal, Silahkan Memesan Item Lagi")
        time.sleep(3)
        menu(items_data)
        handler(items_data)
