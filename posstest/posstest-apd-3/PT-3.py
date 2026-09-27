#APLIKASI ANGKASA
biaya_langganan = 1500000

print("selamat datang di aplikasi angkasa")
print("silahkan login")

nama = input("silahkan masukkan nama : ")
nim  = int(input("silahkan masukkan nim :"))

if nama == "Athar" and nim == 50:
    print("selamat anda telah login hore hore")
    print("silahkan pilih salah satu paket anda boskyuhhh")
    print("1. paket orbit  Biaya administrasi 1%, akses dasar ke lagu-lagu populer ")
    print("2. paket nebula Biaya administrasi 3%, akses lagu premium dan playlist kustom")
    print("3. paket galaxy Biaya administrasi 5%, akses lagu premium, playlist kustom, dan mode offline")
    print("4. paket supernova Biaya administrasi 7%, akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")
    print("input paket nya sesuai nama atau nomor ya kalau nama spasi nya kasi _")
    paket = input("silahkan pilih paket nya boskyuhh: ")
    if paket == "paket_orbit" or paket == "1" :
        total = int(biaya_langganan + biaya_langganan * 0.01)
        print(f"Rp{total}")
        print('''
        akses dasar ke lagu-lagu populer
        gpp kamu pasti lagi hemat duit kan 
        kalau bisa lansung yang max ya
        ''')
    elif paket == "paket_nebula" or paket == "2" :
        total = int(biaya_langganan + biaya_langganan * 0.03)
        print(f"Rp{total}")
        print('''
                akses lagu premium dan playlist kustom
                Dasar Miskin Padahal tinggal nambah dikit
                bisa dapat akses lebih dasar miskin 
                ''')
    elif paket == "paket_galaxy" or paket == "3" :
        total = int(biaya_langganan + biaya_langganan * 0.05)
        print(f"Rp{total}")
        print('''
                akses lagu premium, playlist kustom, dan mode offline
                Dasar kere padahal tinggal dikit lagi 
                bisa dapat paket yang lebih premium dasar 貧乏 
                ''')
    elif paket == "paket supernova" or paket == "4" :
        total = int(biaya_langganan + biaya_langganan * 0.07)
        print(f"Rp{total}")
        print('''
                akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis
                mantap kelas bos kamu orang have ya semoga betah menggunakan aplikasi angkasa
                mantap seakarang kamu bisa mendapatkan konten konten ekslusif artis
                ''')
    else :
        print("tolong pilih paket yang ada dasar gaptek")
else :
    print("login gagal silahkan coba lagi bot")

