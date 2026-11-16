# Contoh error TANPA exception handling (dikomentari, kalau dijalankan program berhenti)
# angka = 10
# hasil = angka / 0
# print("Hasil:", hasil)     # ZeroDivisionError: division by zero


# Menangani exception dengan try-except
try:
    angka = 10
    hasil = angka / 0
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")


# Menangani banyak jenis error
try:
    data = int("abc")          # konversi string ke int gagal
    hasil = 10 / data
except ValueError:
    print("Error: Data tidak valid!")
except ZeroDivisionError:
    print("Error: Tidak boleh membagi dengan nol!")


# Menggunakan else dan finally
try:
    angka = 10 / 2
except ZeroDivisionError:
    print("Error: Tidak bisa bagi nol!")
else:
    print("Perhitungan berhasil, hasil:", angka)    # jalan jika tidak ada error
finally:
    print("Selesai memproses.")                      # selalu jalan


# Membuat exception sendiri dengan raise
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    else:
        print("Umur valid:", umur)


try:
    cek_umur(-5)
except ValueError as e:
    print("Error:", e)
    