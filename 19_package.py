# Menggunakan package
from my_package import operasi, geometri

print(operasi.kurang(10, 4))          # Output: 6
print(geometri.luas_persegi(5))       # Output: 25


# Import fungsi tertentu dari package
from my_package.operasi import kurang
from my_package.geometri import luas_persegi

print(kurang(20, 7))                  # Output: 13
print(luas_persegi(8))                # Output: 64


# Package di Python Standard Library
import os
print(os.getcwd())                    # menampilkan direktori kerja saat ini

import datetime
print(datetime.datetime.today())      # menampilkan tanggal & waktu sekarang
