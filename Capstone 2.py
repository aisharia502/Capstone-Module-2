import math

# Data barang disimpan dalam list of dictionary
toko_pakaian = []  # List

def tampilkan_menu():
    print("\n===== MENU TOKO PAKAIAN =====")
    print("1. Tampilkan Produk")
    print("2. Tambah Produk")
    print("3. Ubah Produk")
    print("4. Hapus Produk")
    print("5. Keluar")

def tampilkan_produk(data):
    if not data:
        print("Belum ada produk yang ditambahkan.")
        return
    print("\nDAFTAR PRODUK:")
    for i, produk in enumerate(data, start=1):
        print(f"{i}. Nama: {produk['nama']} | Kategori: {produk['kategori']} | Harga: {produk['harga']} | Stok: {produk['stok']}")

def tambah_produk():
    nama = input("Nama produk: ")                              # String
    kategori = input("Kategori (Atasan/Celana/Jaket): ")       # String
    harga = float(input("Harga: "))                            # Casting ke float
    stok = int(input("Stok: "))                                # Casting ke int

    produk = {
        "nama": nama,
        "kategori": kategori,
        "harga": harga,
        "stok": stok
    }
    toko_pakaian.append(produk)
    print("Produk berhasil ditambahkan.")

def ubah_produk():
    tampilkan_produk(toko_pakaian)
    index = int(input("Masukkan nomor produk yang ingin diubah: ")) - 1
    if 0 <= index < len(toko_pakaian):
        produk = toko_pakaian[index]
        nama = input(f"Nama [{produk['nama']}]: ") or produk['nama']
        kategori = input(f"Kategori [{produk['kategori']}]: ") or produk['kategori']
        harga_input = input(f"Harga [{produk['harga']}]: ")
        harga = float(harga_input) if harga_input else produk['harga']
        stok_input = input(f"Stok [{produk['stok']}]: ")
        stok = int(stok_input) if stok_input else produk['stok']

        produk.update({
            "nama": nama,
            "kategori": kategori,
            "harga": harga,
            "stok": stok
        })
        print("Produk berhasil diubah.")
    else:
        print("Nomor tidak valid.")

def hapus_produk():
    tampilkan_produk(toko_pakaian)
    index = int(input("Masukkan nomor produk yang ingin dihapus: ")) - 1
    if 0 <= index < len(toko_pakaian):
        if input("Yakin ingin menghapus produk ini? (y/n): ").lower() == 'y':  # If Else Statement
            del toko_pakaian[index]
            print("Produk berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Nomor tidak valid.")

# Function tanpa input/output
def ucapan_terima_kasih():
    print("Terima kasih telah menggunakan sistem toko pakaian.")

# Function dengan input tapi tanpa output
def cetak_nama_kasir(nama):
    print("Kasir hari ini adalah:", nama)

# Function dengan default parameter
def sapa_pengguna(nama="Pengunjung"):
    print(f"Halo, {nama}! Selamat datang di Toko Pakaian.")

# Function dengan input & output
def hitung_total(harga, jumlah):
    total = harga * jumlah
    return total

def main():  # While Loop utama
    sapa_pengguna()                     # Default parameter
    cetak_nama_kasir("Aisyah")          # Function with input

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_produk(toko_pakaian)
        elif pilihan == "2":
            tambah_produk()
        elif pilihan == "3":
            ubah_produk()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "5":
            ucapan_terima_kasih()
            break
        else:
            print("Pilihan tidak tersedia.")

main()

