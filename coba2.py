from abc import ABC, abstractmethod

# === Abstraction & Inheritance ===

class Item(ABC):
    def __init__(self, name, price):
        self.__name = name              # Encapsulation
        self.__price = price            # Encapsulation

    @abstractmethod
    def get_info(self):                # Polymorphism
        pass

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class Service(Item):
    def get_info(self):
        return f"Layanan: {self.get_name()} - Rp{self.get_price():,}"

class Product(Item):
    def get_info(self):
        return f"Produk: {self.get_name()} - Rp{self.get_price():,}"

# === Order dan Pembayaran ===

class Order:
    def __init__(self):
        self.__items = []

    def add_item(self, item: Item):
        self.__items.append(item)

    def calculate_total(self):
        return sum(item.get_price() for item in self.__items)

    def show_order(self):
        print("\n=== RINCIAN PESANAN ===")
        if not self.__items:
            print("Tidak ada item yang dipesan.")
        for item in self.__items:
            print(f"- {item.get_info()}")
        print(f"Total Tagihan: Rp{self.calculate_total():,}")

class Payment:
    def __init__(self, method):
        self.method = method

    def process(self, amount):
        print(f"\n💵 Pembayaran sebesar Rp{amount:,} melalui {self.method} berhasil!")
        print("✅ Transaksi selesai. Terima kasih telah menggunakan layanan kami!")

# === Data Layanan & Produk ===

services = {
    1: Service("Cuci Kering", 10000),
    2: Service("Cuci Basah", 8000),
    3: Service("Self Service", 5000),
    4: Service("Cuci Rapi", 12000),
    5: Service("Cuci Sepatu", 15000),
    6: Service("Cuci Tas", 18000),
    7: Service("Cuci Gorden", 25000),
    8: Service("Cuci Karpet", 30000),
    9: Service("Cuci Boneka", 20000),
    10: Service("Cuci Selimut", 22000),
}

products = {
    1: Product("Deterjen", 10000),
    2: Product("Pemutih", 8000),
    3: Product("Tas Plastik Besar", 5000),
}

payment_methods = ["GoPay", "OVO", "ShopeePay", "Bank", "QRIS", "Tunai"]

# === Fungsi Menu ===

def tampilkan_menu_item(items, title):
    print(f"\n=== {title} ===")
    for key, item in items.items():
        print(f"{key}. {item.get_info()}")
    print("0. Kembali")

def menu_tambah_item(order, items, title):
    while True:
        tampilkan_menu_item(items, title)
        try:
            pilih = int(input("Pilih nomor (0 untuk kembali): "))
            if pilih == 0:
                break
            elif pilih in items:
                order.add_item(items[pilih])
                print(f"✔ {items[pilih].get_name()} ditambahkan ke pesanan.")
            else:
                print("❌ Pilihan tidak valid.")
        except ValueError:
            print("⚠ Masukkan angka yang valid.")

def menu_pilih_pembayaran():
    print("\n=== PILIH METODE PEMBAYARAN ===")
    for i, metode in enumerate(payment_methods, 1):
        print(f"{i}. {metode}")
    while True:
        try:
            pilih = int(input("Pilih metode (angka): "))
            if 1 <= pilih <= len(payment_methods):
                return payment_methods[pilih - 1]
            else:
                print("❌ Pilihan tidak valid.")
        except ValueError:
            print("⚠ Masukkan angka yang valid.")

# === Menu Utama ===

def menu_utama():
    order = Order()
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tambah Layanan Laundry")
        print("2. Tambah Produk Tambahan")
        print("3. Lihat Rincian Pesanan")
        print("4. Proses Pembayaran")
        print("0. Keluar")
        try:
            pilih = int(input("Pilih menu: "))
            if pilih == 1:
                menu_tambah_item(order, services, "DAFTAR LAYANAN")
            elif pilih == 2:
                menu_tambah_item(order, products, "DAFTAR PRODUK")
            elif pilih == 3:
                order.show_order()
            elif pilih == 4:
                total = order.calculate_total()
                if total == 0:
                    print("❌ Anda belum menambahkan item apa pun.")
                else:
                    metode = menu_pilih_pembayaran()
                    bayar = Payment(metode)
                    bayar.process(total)
                    break  # keluar setelah transaksi selesai
            elif pilih == 0:
                print("👋 Terima kasih. Sampai jumpa!")
                break
            else:
                print("❌ Menu tidak tersedia.")
        except ValueError:
            print("⚠ Masukkan angka saja.")

# === Program Utama ===

if __name__ == "__main__":
    menu_utama()
