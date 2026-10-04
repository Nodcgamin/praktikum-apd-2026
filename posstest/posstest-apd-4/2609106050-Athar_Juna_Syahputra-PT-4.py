 
total_kalimantan_gambut = 0
total_kalimantan_mineral = 0
total_sumatera_gambut = 0
total_sumatera_mineral = 0
titik_api = 5  

print("-----------------------------------------")
print("SISTEM REKAPITULASI TITIK API KARHUTLA")
print("-----------------------------------------")

print("silahkan login")

while True:
    username = input("username :").strip().lower()
    password = input("password ").strip()

    if username == "juna" and password == "050":
        print("Login berhasil! Selamat datang,", username)
        break
    else:
        print("username atau password salah silakan coba lagi")

lanjut = "y"
while lanjut == "y":
    print("input data titik-titik api")

    pulau = input("Pulau kalimantan/sumatera : ").strip().lower()
    kategori = ""

    if pulau == "kalimantan":
        lahan = input("Jenis lahan gambut/mineral : ").strip().lower()
        if lahan == "gambut":
            kategori = "kalimantan-gambut"
        elif lahan == "mineral":
            kategori = "kalimantan-mineral"
        else:
            print("Jenis lahan salah Data tidak disimpan.")
    elif pulau == "sumatera":
        lahan = input("Jenis lahan gambut/mineral : ").strip().lower()
        if lahan == "gambut":
            kategori = "sumatera-gambut"
        elif lahan == "mineral":
            kategori = "sumatera-mineral"
        else:
            print("jenis lahan salah data tidak disimpan")
    else:
        print("pulau salah data tidak disimpan")

    if kategori != "":
        hotspot = int(input("jumlah titik api (hotspot) : "))
        luas = hotspot * titik_api
        
        if kategori == "kalimantan-gambut":
            total_kalimantan_gambut += luas
        elif kategori == "kalimantan-mineral":
            total_kalimantan_mineral += luas
        elif kategori == "sumatera-gambut":
            total_sumatera_gambut += luas
        elif kategori == "sumatera-mineral":
            total_sumatera_mineral += luas

        print(f"Kategori {kategori}: {hotspot} titik api = {luas} Hektare")
    while True:
        jawaban = input("apakah masih mau input data titik api lagi (y/t) : ").strip().lower()
        if jawaban == "y" or jawaban == "t":
            break
        print("jawab hanya y atau t saja")
 
    if jawaban == "t":
        break
 

total_semua = (total_kalimantan_gambut + total_kalimantan_mineral
               + total_sumatera_gambut + total_sumatera_mineral)

print("-----------------------------------")
print("RINGKASAN TOTAL LUAS LAHAN TERBAKAR")
print("-----------------------------------")
print(f"kalimantan-gambut  : {total_kalimantan_gambut} Hektare")
print(f"kalimantan-mineral : {total_kalimantan_mineral} Hektare")
print(f"sumatera-gambut    : {total_sumatera_gambut} Hektare")
print(f"sumatera-mineral   : {total_sumatera_mineral} Hektare")
print("========================================================")
print(f"total keseluruhan  : {total_semua} Hektare")
print("========================================================")