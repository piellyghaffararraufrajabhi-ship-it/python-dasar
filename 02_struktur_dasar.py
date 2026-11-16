# Ini adalah komentar satu baris
print("Hello, Python!")  # Perintah untuk mencetak teks

"""
Ini komentar multi-baris.
Biasa dipakai untuk dokumentasi.
"""

# Indentasi: Python memakai 4 spasi untuk menandai blok kode
if True:
    print("Kode ini berada di dalam blok if")
    print("Masih di dalam blok if")
print("Kode ini sudah di luar blok if")

# Input dan output dasar
nama = input("Masukkan nama Anda: ")
print("Halo,", nama)


# Struktur program dengan fungsi main
def main():
    print("Hello dari fungsi main!")


if __name__ == "__main__":
    main()
    