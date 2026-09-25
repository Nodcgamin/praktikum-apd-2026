angka = 12
if angka < 10 :
    print("Angka kurang dari 10")


umur = int(input("Masukkan umur: ")) # Input umur
# Misalkan, umur = 17
if umur >= 17:
    print("Kamu sudah bisa membuat KTP") # Blok if dijalankan karena
else:
    print("Kamu belum bisa membuat KTP") # Blok else tidak dijalankan


kendaraan = input("Masukkan jenis kendaraan anda: ")
if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000
# Menampilkan tarif parkir yang harus dibayar
print("Tarif parkir yang harus dibayar:", tarif_parkir)


angka = int(input("masukkan nilai :"))

if angka > 90 :
    print("A")
elif angka > 80 :
    print("B")
elif angka >= 70 :
    print("C")
elif angka > 50 and angka <= 69 :
    print("D")
else  :
    print("E")

#dadadadada
nilai = 70
penilai = "A" if nilai >+ 85 else "c"
print(penilai)




beli = int(input("silahkan bayar: "))

if beli > 200000 :
    print(beli - beli * 0.3)
elif beli > 100000 :
    print(beli - beli * 0.1)
elif beli <=  100000 :
    print (beli)