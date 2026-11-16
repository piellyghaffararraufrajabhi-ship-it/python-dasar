# Integer (int)
umur = 25
print(umur, type(umur))

# Float
tinggi = 170.5
print(tinggi, type(tinggi))

# String (str)
nama = "Budi"
print(nama, type(nama))

# Boolean (bool)
is_active = True
print(is_active, type(is_active))

# List (mutable, bisa diubah)
buah = ["apel", "jeruk", "mangga"]
print(buah, type(buah))

# Tuple (immutable, tidak bisa diubah)
warna = ("merah", "hijau", "biru")
print(warna, type(warna))

# Dictionary (key-value)
mahasiswa = {"nama": "Budi", "usia": 21, "jurusan": "Informatika"}
print(mahasiswa, type(mahasiswa))

# Set (elemen unik, duplikat otomatis dibuang)
angka = {1, 2, 3, 3, 4, 2}
print(angka, type(angka))

# Konversi tipe data
x = 10
y = float(x)  # int -> float
z = str(x)    # int -> string

print(x, type(x))
print(y, type(y))
print(z, type(z))