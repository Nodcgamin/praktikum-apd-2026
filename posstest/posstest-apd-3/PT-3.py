#APLIKASI ANGKASA
biaya_langganan = 1500000

print("selamat datang di aplikasi angkasa")
print("silahkan login")

nama = input("silahkan masukkan nama: ")
nim  = int(input("silahkan masukkan nim :"))

if nama == "Athar" and nim == 50:
    print("selamat anda telah login hore hore")
    print("pilih paket anda")
    print("paket orbit  Biaya administrasi 1%, akses dasar ke lagu-lagu populer ")
    print("paket nebula Biaya administrasi 3%, akses lagu premium dan playlist kustom")
    print("paket galaxy Biaya administrasi 5%, akses lagu premium, playlist kustom, dan mode offline")
    print("paket supernova Biaya administrasi 7%, akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")
    paket = input("silahkan pilih paket anda boskyuhh: ")
    if paket == "paket_orbit" :
        print(int(biaya_langganan + biaya_langganan * 0.01))
        print("akses dasar ke lagu-lagu populer gpp lagi hemat duit ya")
    elif paket == "paket_nebula" :
        print(int(biaya_langganan + biaya_langganan * 0.03))
        print("akses lagu premium dan playlist kustom ga sekalian yg mahal dikit dasar miskin")
    elif paket == "paket_nebula" :
        print(int(biaya_langganan + biaya_langganan * 0.05))
        print("akses lagu premium, playlist kustom, dan mode offline tinggal nambah dikit aja ga bisa dasar kere")
    elif paket == "paket supernova" :
        print(int(biaya_langganan + biaya_langganan * 0.07))
        print("akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis, mantap kelas bos kamu orang have ya mantap seakarang kamu bisa mendapatkan konten konten tersembunyi")
    else :
        print("tolong pilih paket yang ada dasar gaptek")
else :
    print("login gagal silahkan coba lagi bot")

