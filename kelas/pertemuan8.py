import random
import datetime

# Variabel yang menyimpan pilihan karakter angka
angka = "0123456789"

# Mengambil 6 karakter acak dari variabel angka, lalu menggabungkannya menjadi satu string
pin = "".join(random.choices(angka, k=6))

# Mendapatkan tanggal saat ini
waktu_sekarang = datetime.datetime.now()

# Memformat tanggal menggunakan strftime dengan format Hari/Bulan/Tahun
tanggal_dibuat = waktu_sekarang.strftime("%d/%m/%Y")

# Menampilkan hasil
print(f"Kode PIN Keamanan: {pin}")
print(f"Tanggal Pembuatan: {tanggal_dibuat}")