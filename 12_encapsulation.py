# Level akses atribut
class Contoh:
    def __init__(self):
        self.publik = "bisa diakses di mana saja"
        self._protected = "konvensi: jangan diakses dari luar class"
        self.__private = "tidak bisa diakses dari luar class"


c = Contoh()
print(c.publik)
print(c._protected)    # masih bisa, tapi hanya konvensi
# print(c.__private)   # ERROR: AttributeError


# Encapsulation dengan private attribute
class BankAccount:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal    # private attribute

    # getter
    def lihat_saldo(self):
        return self.__saldo

    # setter
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus positif!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")


# Membuat objek
akun = BankAccount(1000)

# Mengakses saldo lewat method (getter)
print("Saldo awal:", akun.lihat_saldo())

akun.setor(500)
print("Setelah setor:", akun.lihat_saldo())

akun.tarik(300)
print("Setelah tarik:", akun.lihat_saldo())

# Validasi bekerja: setor negatif dan tarik melebihi saldo ditolak
akun.setor(-100)
akun.tarik(5000)