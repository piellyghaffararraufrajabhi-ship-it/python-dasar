# Konstanta: ditulis HURUF KAPITAL, pisahkan kata dengan underscore
PI = 3.14159
MAX_USERS = 100
APP_NAME = "Aplikasi Belajar Python"

print(PI)
print(MAX_USERS)
print(APP_NAME)

# PI = 3.14   # TIDAK disarankan: mengubah nilai konstanta

# Mengimpor konstanta dari module lain
from konstanta import PI, GRAVITY, MAX_RETRY

print("Nilai PI:", PI)
print("Gravitasi:", GRAVITY)
print("Maksimum Percobaan:", MAX_RETRY)

# Contoh penggunaan konstanta: menghitung pajak
TAX_RATE = 0.1  # 10% pajak

harga_barang = 50000
total = harga_barang + (harga_barang * TAX_RATE)

print("Total harga:", total)