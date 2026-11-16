# Menggunakan module buatan sendiri
import matematika

print(matematika.tambah(3, 2))    # Output: 5
print(matematika.kali(4, 5))      # Output: 20


# Import dengan alias
import matematika as m

print(m.tambah(10, 5))            # Output: 15


# Import fungsi tertentu
from matematika import tambah

print(tambah(7, 2))               # Output: 9


# Built-in module: math
import math

print(math.sqrt(16))              # akar kuadrat -> 4.0
print(math.pi)                    # konstanta pi -> 3.141592653589793