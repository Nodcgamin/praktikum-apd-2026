import os
os.system("cls" if os.name == "nt" else "clear")
# def luas_persegi_panjang(panjang, lebar):
#     panjang = int(input("MASUKKAN ANGKA : "))
#     lebar = int(input("masukkan angka : "))
#     luas = panjang * lebar
#     return luas

# print("Luas persegi panjang:", luas_persegi_panjang())

# def total_harga_tanah(panjang, lebar, harga = 100000):
#     total = luas_persegi_panjang(panjang, lebar) * harga
#     return total
# print("Total harga tanah:", total_harga_tanah())

# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas
# #Kita panggil fungsinya
# print("Luas persegi panjang:", luas_persegi_panjang())

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# hasil = luas_persegi(int(input("masukkan angka : ")))
# print("Luas persegi:", hasil)


# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     return luas
# def total_harga_tanah(panjang, lebar, harga = 100000):
#     total = luas_persegi_panjang(panjang, lebar) * harga
#     return total
# #Kita panggil fungsinya
# print("Luas persegi panjang:", luas_persegi_panjang(7, 4))
# print("Total harga tanah:", total_harga_tanah(7, 4))

# def pengumuman():
#     print("posstest nya kerjakan")
# for i in range(2):

#     pengumuman()

# def sapa_pengguna(nama_pengguna):
#     print(f"Halo, selamat datang {nama_pengguna}")

# sapa_pengguna(input("masukkan : "))

# def keliling_persegi(sisi):
#     keliling = sisi * 4
#     print("keliling persegi  : ", keliling)
# keliling_persegi(int(input("masukkan sisi : ")))


# nama = "Larry"
# prodi = "Informatika"
# #Membuat variabel lokal
# def data():
#     nama = "Teknik Kedokteran"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)

# data() 


# print("Nama:", nama)
# print("Prodi:", prodi)


# def faktorial(n):
# #Base Case: Kondisi fungsi berhenti
#     if n == 0 or n == 1:
#         return 1

#     else:
#         return n * faktorial(n - 1)

# hasil_faktorial = faktorial(int(input("masukkan angka : ")))
# print(f"Hasil dari 4! {hasil_faktorial}")


# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else :
#     print(f'Angka yang kamu input : {angka}')
# finally : 
#     print("posstest selesai")


try:
    usn = input('Username yang diinginkan : ')
    if len(usn) < 5:
        raise ValueError('Nama Minimal Memiliki 5 karakter')
except ValueError as e:
    print(e)
else : 
    print(usn)