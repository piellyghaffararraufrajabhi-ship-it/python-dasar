# Membuat function sederhana
def sapa():
    print("Halo, selamat datang di Python!")

# Memanggil function
sapa()


# Function dengan parameter
def sapa_nama(nama):
    print(f"Halo {nama}, semoga harimu menyenangkan!")

sapa_nama("Budi")
sapa_nama("Dita")


# Function dengan return value
def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print("Hasil penjumlahan:", hasil)


# Default parameter
def sapa_orang(nama="Teman"):
    print(f"Halo {nama}!")

sapa_orang("Andi")   # menggunakan parameter
sapa_orang()         # menggunakan default


# *args: jumlah argumen tidak terbatas
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4, 5)


# **kwargs: argumen berupa pasangan key-value
def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Budi", umur=20, kota="Jakarta")