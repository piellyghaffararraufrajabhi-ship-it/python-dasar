# Membuat variable
nama = "Budi"
umur = 25
tinggi = 170.5
is_active = True

print(nama)
print(umur)
print(tinggi)
print(is_active)

# Aturan penamaan: gunakan snake_case
first_name = "Budi"
total_harga = 10000
print(first_name)
print(total_harga)

# Contoh nama yang SALAH (dikomentari agar program tidak error)
# 2nama = "Salah"      # diawali angka
# for = "Informatika"   # memakai keyword Python

# Multiple assignment: beberapa variable sekaligus
a, b, c = 10, 20, 30
print(a, b, c)

# Satu nilai untuk beberapa variable
x = y = z = 100
print(x, y, z)

# Mengecek tipe data variable
print(type(nama))
print(type(umur))
print(type(tinggi))

# Menghapus variable dengan del
x = 10
print(x)

del x

try:
    print(x)
except NameError as e:
    print("Error:", e)
    