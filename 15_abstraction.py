from abc import ABC, abstractmethod


# Abstract class
class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass


# Subclass yang mengimplementasikan abstract method
class Kucing(Hewan):
    def suara(self):
        return "Meow"


class Anjing(Hewan):
    def suara(self):
        return "Guk guk"


# Tidak bisa langsung membuat objek dari class abstract
# h = Hewan()   # ERROR: TypeError

# Harus buat dari subclass
k = Kucing()
a = Anjing()

print(k.suara())
print(a.suara())


# Abstraction di dunia nyata: sistem pembayaran
class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass


class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan GoPay")


class Bank(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan Bank")


# Menggunakan abstraction
def proses_pembayaran(metode, jumlah):
    metode.bayar(jumlah)


# Mengirim objek berbeda, satu fungsi
proses_pembayaran(Gopay(), 50000)
proses_pembayaran(Bank(), 70000)