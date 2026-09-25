biaya_langganan = 1500000

print("==========================================")
print("     WELCOME TO MUSIC APP ANGKASA 🎵      ")
print("==========================================")
print("Silahkan login terlebih dahulu\n")

nama = input("silahkan masukkan nama : ")
nim  = int(input("silahkan masukkan nim  : "))

if nama == "Athar" and nim == 50:
    print("\n==========================================")
    print("  selamat anda telah login hore hore 🎉   ")
    print("==========================================")
    
    print("\n--- PILIHAN PAKET ANGKASA ---")
    print("1. paket orbit     : Biaya admin 1%")
    print("2. paket nebula    : Biaya admin 3%")
    print("3. paket galaxy    : Biaya admin 5%")
    print("4. paket supernova : Biaya admin 7%")
    print("------------------------------------------")
    
    paket = input("silahkan pilih paket anda boskyuhh : ").lower().strip()
    
    # Inisialisasi variabel untuk menampung data
    admin_persen = 0
    nama_paket = ""
    fitur = ""
    pesan_humor = ""

    # Pilihan Percabangan Paket
    if paket == "paket orbit" or paket == "1":
        nama_paket = "Paket Orbit"
        admin_persen = 0.01
        fitur = "Akses dasar ke lagu-lagu populer"
        pesan_humor = "gpp lagi hemat duit ya 😉"
        
    elif paket == "paket nebula" or paket == "2":
        nama_paket = "Paket Nebula"
        admin_persen = 0.03
        fitur = "Akses lagu premium dan playlist kustom"
        pesan_humor = "ga sekalian yg mahal dikit? 😜"
        
    elif paket == "paket galaxy" or paket == "3":
        nama_paket = "Paket Galaxy"
        admin_persen = 0.05
        fitur = "Akses lagu premium, playlist kustom, dan mode offline"
        pesan_humor = "tinggal nambah dikit lagi padahal~ 😁"
        
    elif paket == "paket supernova" or paket == "4":
        nama_paket = "Paket Supernova"
        admin_persen = 0.07
        fitur = "Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"
        pesan_humor = "mantap kelas bos! kamu orang kaya ya, sekarang bisa akses konten tersembunyi 🔥🚀"
        
    else:
        print("\n❌ Tolong pilih paket yang ada!")