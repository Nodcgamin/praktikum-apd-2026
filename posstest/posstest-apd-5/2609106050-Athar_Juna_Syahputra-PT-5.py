import os

user = [["bos","gamin","admin"]]
map_pool = ["dread", "kreaster", "kitres","bortologo"]
riwayat = []

user_ada = None


while True :
    os.system("cls" if os.name == "nt" else "clear")

    if user_ada == None :
        print("Sistem Pencatatan game")
        print("1. login")
        print("2. register ")
        print("3. logout")
        pilih = int(input("silahkan pilih menu:"))

        if pilih == 1 :
            username = input("masukkan nama: ").lower()
            password = input("massukan password:")
            for u in user :
                if u[0] == username and u[1] == password :
                    user_ada = u 
            if user_ada == None :
                print("username atau password salah")
                input("tekan enter untuk kembali...")
        elif  pilih == 2:
            print("Regis Bos Ku")
            username = input("Masukkan Username:").lower()
            password = input("Masukkan Password:")
            sudah_terambil = False
            for u in user :
                if u[0] == username :
                    sudah_terambil = True
            if username == "" or password == "":
                print("masukkan username dan password tidak boleh kosong tolol")
            elif sudah_terambil:
                print("yah sudah ke ambil")
            else :
                user.append([username,password,"user"])
                print("Mantap silahkan Login")
            input("tekan enter untuk kembali...")
        elif pilih == 3:
            print("tamatlah sudah cerita kami")
            break
        else :
            print("pilih yang benar dong")
            input("tekan enter untuk kembali...")
    elif user_ada[2] == "user":
        nama = user_ada[0]
        print(" Menu login sebagai = "  + nama )
        print("1. Tambah Riwayat Game")
        print("2. Lihat Riwayat Game Saya")
        print("3. Lihat Winrate Total & Per Map")
        print("4. Lihat Statistik Satu Map")
        print("0. Logout")
        pilih = input("Pilih menu: ")

        if pilih == 1 :
            print("TAMBAH RIWAYAT GAME")    
            nomor_map = 0
            for m in map_pool :
                nomor_map += 1
                print(f"{nomor_map}. {m}")
            pilihan = input("silahkan pilih nomor map: ")
            if pilihan.isdigit() and 1 <= int(pilihan) <= nomor_map:
                nama_map = map_pool[int(pilihan) - 1]
                character = input("masukkan nama character: ")
                kill = input("Kill : ")
                death = input("Death : ")
                assist = input("Assist : ")
                print("1.Menang, 2. Kalah")
                result = input("Menang atau Kalah : ")
                if kill.isdigit() and death.isdigit() and assist.isdigit() and result in ["1" , "2"]:
                    teks_result = "Menang" if result == "1" else "kalah"
                    riwayat.append([nama, nama_map, character, int(kill), int(death), int(assist), teks_result]) 
                    print("riwayat game telah ditambah boskyuuu")        
                else :
                    print("INPUT K/D/A YANG BENAR DONG") 
            else :
                print("INPUT MAP YANG BENAR DONG")        
            input("tekan enter untuk kembali...")
        elif pilih == "2" :
            print(" RIWAYAT GAME MU BOSKYUU")
            nomor_game = 0
            for r in riwayat:
                if r[0] == nama:
                    nomor_game += 1
                    print(f"{nomor_game}. {r[1]}  {r[2]}  K/D/A {r[3]}/{r[4]}/{r[5]}  {r[6]}")
            if nomor_game == 0:
                print("Belum ada riwayat game.")
            input("tekan enter untuk kembali...")
        elif pilih == "3":
            total = 0
            menang = 0
            kill_total = 0
            death_total = 0
            assist_total = 0
            for r in riwayat:
                if r[0] == nama :
                    total += 1 
                    kill_total += r[3]
                    death_total += r[4]
                    assist_total += r[5]
                    if r[6] == "Menang" :
                        menang += 1
            print("STATISTIK TOTAL")
            if total == 0:
                print("Belum ada data game.")
            else:
                winrate = menang / total * 100
                print(f"Total game : {total}")
                print(f"Menang     : {menang}")
                print(f"Kalah      : {total - menang}")
                print(f"Winrate    : {winrate:.1f}%")
                print(f"Total K/D/A: {kill_total}/{death_total}/{assist_total}")
                print("WINRATE PER MAP")
                for m in map_pool:
                    t_map = 0
                    w_map = 0
                    for r in riwayat:
                        if r[0] == nama and r[1] == m :
                            t_map += 1
                            if r[6] ==  "Menang":
                                w_map += 1
                    if t_map == 0:
                        print(f"{m}: belum pernah dimainkan")
                    else :
                        print(f"{m}: {w_map}/{t_map} menang | winrate {w_map / t_map * 100:.1f}%")
            input("tekan enter untuk kembali...")

        elif pilih == "4":
            print("STATISTIK SATU MAP")
            nomor_map = 0
            for m in map_pool:
                nomor_map += 1
                print(f"{nomor_map}. {m}")
            pilihan = input("pilih nomor mapnya boskyuuu: ")
            if pilihan.isdigit() and 1 <= int(pilihan) <= nomor_map:
                m = map_pool[int(pilihan) - 1]
                t_map = 0
                w_map = 0
                k_map = 0
                d_map = 0
                a_map = 0
                print(f"Statistik map {m}:")
                for r in riwayat:
                    if r[0] == nama and r[1] == m:
                        t_map += 1
                        k_map += r[3]
                        d_map += r[4]
                        a_map += r[5]
                        if r[6] == "Menang":
                            w_map += 1
                        print(f"{r[2]} K/D/A {r[3]}/{r[4]}/{r[5]} {r[6]}")
                if t_map == 0:
                    print("Belum ada game di map ini.")
                else:
                    print(f"\nTotal game : {t_map}")
                    print(f"Menang     : {w_map}")
                    print(f"Kalah      : {t_map - w_map}")
                    print(f"Winrate    : {w_map / t_map * 100:.1f}%")
                    print(f"Total K/D/A: {k_map}/{d_map}/{a_map}")
            else:
                print("Nomor map tidak valid!")
            input("tekan enter untuk kembali...")
 
        elif pilih == "0":
            user_ada = None
 
        else:
            print("Menu tidak valid!")
            input("tekan enter untuk kembali...")

    else:
        print("  <MENU ADMIN>   login: " + user_ada[0])
        print("1. Lihat Map Pool")
        print("2. Tambah Map Baru")
        print("3. Ganti Nama Map")
        print("4. Lihat Daftar Pengguna")
        print("5. Lihat Semua Riwayat Game")
        print("6. Reset Statistik (Season Baru)")
        print("0. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            print("MAP POOL SAAT INI")
            nomor_map = 0
            for m in map_pool:
                nomor_map += 1
                print(f"{nomor_map}. {m}")
            input("Tekan Enter untuk kembali...")

        elif pilih == "2" :
            print("TAMBAH MAP BARU")
            nama_map = input("nama map barunya MY BROOOO : ")
            ada = False
            for m in map_pool:
                if m.lower() == nama_map.lower():
                    ada = True
            if nama_map == "":
                print("GAK BOLEH KOSONG DONNG")
            elif ada:
                print("MINES LITERASI DONGO")
            else:
                map_pool.append(nama_map)
                print(f"Map {nama_map} berhasil ditambahkan mantap mantap mantap")
            input("tekan Enter untuk kembali...")

        elif pilih == "3":
            print(" GANTI NAMA MAP ")
            nomor_map = 0
            for m in map_pool:
                nomor_map += 1
                print(f"{nomor_map}. {m}")
            pilihan = input("Nomor map yang ingin diganti broskkiiiiii : ")
            if pilihan.isdigit() and 1 <= int(pilihan) <= nomor_map:
                gx = int(pilihan) - 1
                lama = map_pool[gx]
                baru = input("Nama map pengganti nya bro: ")
                if baru == "":
                    print("GAK BOLEH KOSONG DONG")
                else:
                    map_pool[gx] = baru
                    for r in riwayat:
                        if r[1] == lama:
                            r[1] = baru
                    print(f"Map {lama} berhasil diganti dengan {baru}")
            else:
                print("PILIH YANG BENAR DONG ASTAGA")
            input("tekan Enter untuk kembali...")
        
        elif pilih == "4":
            print(" DAFTAR PENGGUNA ")
            for u in user:
                total = 0
                for r in riwayat:
                    if r[0] == u[0]:
                        total += 1
                print(f" {u[0]} ({u[2]}) total game: {total}")
            input("Tekan Enter untuk kembali...")

        elif pilih == "5":
            print("SEMUA RIWAYAT GAME ")
            if riwayat == []:
                print("YAH BELUM ADA YANG MASUKKIN")
            for r in riwayat:
                print(f"{r[0]} {r[1]}  {r[2]} K/D/A {r[3]}/{r[4]}/{r[5]} {r[6]}")
            input("tekan Enter untuk kembali...")

        elif pilih == "6":
            print(" RESET STATISTIK ")
            print("1. Reset semua pengguna")
            print("2. Reset satu pengguna")
            sub = input("Pilih: ")
            if sub == "1":
                konfirmasi = input("Yakin nih yakin nih hapus semua stat (ya/tidak): ").lower()
                if konfirmasi == "ya":
                    riwayat = []
                    print("semua stat berhasil direset. NEW SEASON NEW ME")
                else:
                    print("YAAA GA JADI")
            elif sub == "2":
                target = input("Username yang direset: ").lower()
                konfirmasi = input(f"Yakin reset satu pengguna aja katanya solid parah sih {target}? (ya/tidak): ").lower()
                if konfirmasi == "ya":
                    sisa = []
                    for r in riwayat:
                        if r[0] != target:
                            sisa.append(r)
                    riwayat = sisa
                    print(f"Statistik {target} berhasil direset.")
                else:
                    print("YAAA GA JADI")
            else:
                print("PILIH YANG BENAR DONG MIN")
            input("tekan Enter untuk kembali...")
 
        elif pilih == "0":
            user_ada = None
 
        else:
            print("PILIH YANG BENAR DONG ASTAGA")
            input("tekan Enter untuk lanjut...")
 