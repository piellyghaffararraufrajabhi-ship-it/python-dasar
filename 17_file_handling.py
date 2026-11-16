# Persiapan: buat file data.txt berisi satu baris teks
file = open("data.txt", "w")
file.write("Halo Dunia")
file.close()

# Membuka dan membaca file
file = open("data.txt", "r")    # "r" = read
print(file.read())              # membaca seluruh isi file sekaligus
file.close()                    # wajib ditutup setelah dipakai


# Persiapan: isi data.txt dengan 2 baris
file = open("data.txt", "w")
file.write("Baris 1\nBaris 2\n")
file.close()

# Membaca file baris per baris
file = open("data.txt", "r")
for baris in file:
    print(baris.strip())        # strip() membuang karakter newline (\n)
file.close()


# Menulis ke file (isi lama akan DITIMPA)
file = open("data.txt", "w")    # "w" = write
file.write("Halo, ini data baru!\n")
file.write("Baris kedua...\n")
file.close()

file = open("data.txt", "r")
print(file.read(), end="")
file.close()


# Menambah data ke akhir file (isi lama tidak hilang)
file = open("data.txt", "a")    # "a" = append
file.write("Baris tambahan...\n")
file.close()

file = open("data.txt", "r")
print(file.read(), end="")
file.close()


# Menggunakan with (best practice): file otomatis ditutup
with open("data.txt", "r") as file:
    isi = file.read()
    print(isi, end="")


# Contoh Program Lengkap
# Menulis file (isi lama ditimpa)
with open("contoh.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

# Menambah data
with open("contoh.txt", "a") as file:
    file.write("Tambahan baris kedua.\n")

# Membaca file baris per baris
with open("contoh.txt", "r") as file:
    for baris in file:
        print(baris.strip())