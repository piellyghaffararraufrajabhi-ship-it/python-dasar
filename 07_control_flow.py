# Percabangan (if, elif, else)
nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
else:
    print("C")

# Perulangan for
buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(item)

# Perulangan while
count = 0

while count < 5:
    print("Hitung:", count)
    count += 1

# Break dan Continue
for i in range(1, 10):
    if i == 2:
        continue    # lewati angka 2
    if i == 5:
        break       # hentikan loop saat i == 5
    print(i)