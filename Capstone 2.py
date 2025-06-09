import uuid

# Data barang disimpan dalam list of dictionary
baju_list = []

def tampilkan_menu():
    print("\n===== TOKO BAJU BOOSANA  =====")
    print("1. Tampilkan Data Baju")
    print("2. Tambah Produk")
    print("3. Ubah Produk")
    print("4. Hapus Produk")
    print("5. Exit")

def tampilkan_baju(data):
    if not data:
        print("Belum ada data baju.")
        return
    print("\nDATA BAJU TOKO:")
    for baju in data:
        print(f"UID: {baju['uid']} | Nama: {baju['nama']} | Kategori: {baju['kategori']} | Harga: Rp {int(baju['harga']):,} | Stok: {baju['stok']}")

def cari_baju_berdasarkan_uid(uid):
    for baju in baju_list:
        if baju['uid'] == uid:
            return baju
    return None

def konfirmasi_aksi(pesan="Apakah Anda yakin? (y/n): "):
    konfirmasi = input(pesan)
    return konfirmasi.lower() == "y"

def tambah_baju():
    nama = input("Nama baju: ")
    kategori = input("Kategori baju: ")
    harga = float(input("Harga baju: "))
    stok = int(input("Stok baju: "))
    uid_baju = str(uuid.uuid4())[:8]
    baju = {
        "uid": uid_baju,
        "nama": nama,
        "kategori": kategori,
        "harga": harga,
        "stok": stok
    }
    baju_list.append(baju)
    print("Barang berhasil ditambahkan.")

def ubah_baju():
    uid = input("Masukkan UID baju yang ingin diubah: ")
    baju = cari_baju_berdasarkan_uid(uid)
    if baju:
        print("Baju ditemukan.")
        nama = input(f"Nama [{baju['nama']}]: ") or baju['nama']
        kategori = input(f"Kategori [{baju['kategori']}]: ") or baju['kategori']
        harga_input = input(f"Harga [{baju['harga']}]: ")
        harga = float(harga_input) if harga_input else baju['harga']
        stok_input = input(f"Stok [{baju['stok']}]: ")
        stok = int(stok_input) if stok_input else baju['stok']

        baju.update({
            "nama": nama,
            "kategori": kategori,
            "harga": harga,
            "stok": stok
        })
        print("Baju berhasil diubah.")
    else:
        print("Baju tidak ditemukan.")

def hapus_baju():
    uid = input("Masukkan UID baju yang ingin dihapus: ")
    baju = cari_baju_berdasarkan_uid(uid)
    if baju:
        tampilkan_baju([baju])
        if konfirmasi_aksi("Yakin ingin menghapus baju ini? (y/n): "):
            baju_list.remove(baju)
            print("Baju berhasil dihapus.")
    else:
        print("Baju tidak ditemukan.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_baju(baju_list)
        elif pilihan == "2":
            tambah_baju()
        elif pilihan == "3":
            ubah_baju()
        elif pilihan == "4":
            hapus_baju()
        elif pilihan == "5":
            print("Keluar dari program. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

main()
