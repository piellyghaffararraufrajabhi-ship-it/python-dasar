# Membuat dictionary
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa)


# Mengakses data
print(mahasiswa["nama"])        # Budi
print(mahasiswa.get("umur"))    # 20

# Jika key tidak ada, get() mengembalikan None (tidak error)
print(mahasiswa.get("alamat"))  # None


# Menambah dan mengubah data
mahasiswa["angkatan"] = 2023    # menambah key baru
mahasiswa["umur"] = 21          # mengubah value yang sudah ada

print(mahasiswa)


# Menghapus data
mahasiswa.pop("jurusan")        # menghapus dengan pop
del mahasiswa["nama"]           # menghapus dengan del

print(mahasiswa)


# Iterasi dictionary
for key, value in mahasiswa.items():
    print(key, ":", value)


# Nested dictionary
kampus = {
    "mahasiswa1": {"nama": "Budi", "umur": 21},
    "mahasiswa2": {"nama": "Dita", "umur": 22}
}

print(kampus["mahasiswa1"]["nama"])    # Budi
