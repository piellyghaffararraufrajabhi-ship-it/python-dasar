# Operator Aritmatika
a = 10
b = 3

print(a + b)    # penjumlahan
print(a - b)    # pengurangan
print(a * b)    # perkalian
print(a / b)    # pembagian (float)
print(a // b)   # pembagian bulat
print(a % b)    # sisa bagi (modulus)
print(a ** b)   # pangkat

# Operator Perbandingan
x = 5
y = 10

print(x == y)   # sama dengan
print(x != y)   # tidak sama dengan
print(x > y)    # lebih besar
print(x < y)    # lebih kecil
print(x >= y)   # lebih besar atau sama dengan
print(x <= y)   # lebih kecil atau sama dengan

# Operator Logika
p = True
q = False

print(p and q)  # benar jika keduanya benar
print(p or q)   # benar jika salah satu benar
print(not p)    # membalikkan nilai

# Operator Penugasan
n = 10
n += 5
print(n)        # 15
n -= 3
print(n)        # 12
n *= 2
print(n)        # 24
n /= 4
print(n)        # 6.0

# Operator Keanggotaan (Membership)
buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)          # True
print("pisang" not in buah)    # True

# Operator Identitas
list_a = [1, 2, 3]
list_b = list_a        # list_b menunjuk objek yang SAMA dengan list_a
list_c = [1, 2, 3]     # objek baru dengan isi yang sama

print(list_a is list_b)        # True  (objek yang sama)
print(list_a is list_c)        # False (objek berbeda)
print(list_a == list_c)        # True  (isinya sama)