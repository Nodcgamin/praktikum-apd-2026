"""
Project 1 - Sistem Kasir Kantin Kampus (Rian & Yaya)
Materi: Algoritma, Pseudocode, Flowchart, Percabangan (If-Else), Pengulangan (Looping)
"""

DISKON_MAHASISWA = 0.10  # diskon 10% untuk mahasiswa


def baca_angka(pesan, minimal=1):
    """Meminta input angka bulat; mengulang sampai valid."""
    while True:
        try:
            nilai = int(input(pesan))
            if nilai >= minimal:
                return nilai
            print(f"  Nilai minimal {minimal}.")
        except ValueError:
            print("  Input harus berupa angka bulat.")


def main():
    print("=" * 40)
    print("   SISTEM KASIR KANTIN KAMPUS")
    print("=" * 40)

    lanjut = "Y"
    total_hari_ini = 0

    # PENGULANGAN (Looping): ulangi selama kasir menjawab 'Ya'
    while lanjut == "Y":
        # INPUT pesanan (jajargenjang di flowchart)
        menu = input("\nNama menu         : ").strip()
        harga = baca_angka("Harga satuan (Rp) : ")
        jumlah = baca_angka("Jumlah            : ")
        status = input("Mahasiswa? (y/n)  : ").strip().lower()

        # PROSES hitung total (persegi panjang)
        total = harga * jumlah

        # PERCABANGAN If-Else (belah ketupat)
        if status == "y":          # True  -> dapat diskon
            potongan = total * DISKON_MAHASISWA
            total = total - potongan
            keterangan = f"Diskon mahasiswa {int(DISKON_MAHASISWA * 100)}%"
        else:                      # False -> harga normal
            keterangan = "Harga normal"

        # OUTPUT (jajargenjang)
        print(f"\n  {jumlah} x {menu}")
        print(f"  {keterangan}")
        print(f"  TOTAL BAYAR : Rp {int(total):,}".replace(",", "."))

        total_hari_ini += total

        # Input 'lanjut' ada DI DALAM loop (perbaikan bug infinite loop)
        lanjut = input("\nPesanan baru? (Y/T) : ").strip().upper()

    print("\n" + "-" * 40)
    print(f"Total pemasukan hari ini : Rp {int(total_hari_ini):,}".replace(",", "."))
    print("Terima kasih, selamat makan!")


if __name__ == "__main__":
    main()