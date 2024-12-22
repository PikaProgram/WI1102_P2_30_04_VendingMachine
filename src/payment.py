# Logika pembayaran
def payment(payment_method, items_data, item_data):
    using_code = input("Apakah Anda Ingin Menggunakan Kode Promo? (y)a/(t)idak: ").lower() == "y"
    # Jika menggunakan kode promo
    discount = 0
    valid_code = False
    if using_code:
        promo_code = input("Masukan Kode Promo: kode/(b)atal ").upper()
        while promo_code != "b" and valid_code == False:
            code_lines = open("data/kode.csv", "r").readlines()
            for code in code_lines:
                code_data = code.strip().split(",")
                if (code_data[1] == item_data[3] and code_data[0] == promo_code):
                    valid_code = True
                    discount = int(code_data[2])/100.0
                    code_lines.remove(code)
                    break
            if valid_code:
                print("Kode Promo Valid, Diskon Sebesar ", discount * 100, "%")
                code_file = open("data/kode.csv", "w") 
                code_file.write("\n".join(code_lines))
                code_file.close()
                break
            else:
                print("Kode Promo Tidak Valid, Silahkan Masukan Kode Promo Yang Valid")
                promo_code = input("Masukan Kode Promo [kode/(b)atal]: ").upper()

    balanced_owed = (1-discount) * int(item_data[2].replace(".", ""))

    # Jika input "q", pembayaran menggunakan qris
    if payment_method == "q":
        print("Total Yang Harus Dibayar: ", int(balanced_owed))
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
        success = input("Silahkan Bayar Menggunakan QR Di Atas (y)a/(t)idak: ").lower() == "y"
        return success
    # Jika input "t", pembayaran menggunakan tunai
    elif payment_method == "t":
        balance_paid = 0
        # Logika transaksi tunai
        print("Total Yang Harus Dibayar: ", int(balanced_owed))
        while balanced_owed > balance_paid:
            cash_input = input("Silahkan Masukan Uang Tunai (5/10/20/50/75/100/(b)atal): ")
            if cash_input == "b":
                payment("b", items_data, item_data)
            elif cash_input in ["5", "10", "20", "50", "75", "100"]:
                balance_paid += int(cash_input) * 1000
        return True