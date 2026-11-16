# ===== LIST (mutable, bisa diubah) =====
buah = ["apel", "jeruk", "mangga"]

print(buah[0])            # akses elemen -> apel

buah.append("pisang")     # menambahkan elemen
buah[1] = "anggur"        # mengubah elemen
buah.remove("mangga")     # menghapus elemen

print(buah)


# ===== TUPLE (immutable, tidak bisa diubah) =====
warna = ("merah", "hijau", "biru")

print(warna[1])           # akses elemen -> hijau

# Tuple tidak bisa diubah setelah dibuat
# warna[0] = "kuning"     # ERROR: TypeError

# Tapi bisa di-loop dengan for
for w in warna:
    print(w)


# ===== SET (unik, tidak berurutan) =====
angka = {1, 2, 3, 3, 4, 5}
print(angka)              # duplikat otomatis hilang

angka.add(6)              # menambahkan elemen
angka.remove(2)           # menghapus elemen
print(angka)

# Operasi himpunan
ganjil = {1, 3, 5, 7}
genap = {2, 4, 6, 8}

print(ganjil | genap)     # union (gabungan)
print(ganjil & genap)     # intersection (irisan)
print(ganjil - genap)     # difference (selisih)
