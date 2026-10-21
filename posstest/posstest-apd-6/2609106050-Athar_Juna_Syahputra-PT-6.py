import os

user = [
    {"username": "bos", "password": "gamin", "role": "admin"}
]
map_pool = {1: "dread", 2: "kreaster", 3: "kitres", 4: "bortologo"}
riwayat = {}

user_ada = None


while True :
    os.system("cls" if os.name == "nt" else "clear")

    if user_ada == None :
        print("Sistem Pencatatan game")
        print("1. login")
        print("2. register ")
        print("3. logout")
        pilih = input("silahkan pilih menu:")

        if pilih.isdigit() == "1" :
            username = input("masukkan nama: ").lower()
            password = input("massukan password:")
            for u in user :
                if u["username"] == username and u["password"] == password :
                    user_ada = u
            if user_ada == None :
                print("username atau password salah")
                input("tekan enter untuk kembali...")
        elif  pilih.isdigit() == "2":
            print("Regis Bos Ku")
            username = input("Masukkan Username:").lower()
            password = input("Masukkan Password:")
            sudah_terambil = False
            for u in user :
                if u["username"] == username :
                    sudah_terambil = True
            if username == "" or password == "":
                print("masukkan username dan password tidak boleh kosong tolol")
            elif sudah_terambil:
                print("yah sudah ke ambil")
            else :
                user.append ({"username": username, "password": password, "role": "user"})
                print("Mantap silahkan Login")
            input("tekan enter untuk kembali...")
        elif pilih.isdigit() == "3":
            print("tamatlah sudah cerita kami")
            break
        else :
            print("pilih yang benar dong")
            input("tekan enter untuk kembali...")
    elif user_ada["role"] == "user":
        nama = user_ada["username"]
        print(" Menu login sebagai = "  + nama )
        print("1. Tambah Riwayat Game")
        print("2. Lihat Riwayat Game Saya")
        print("3. Lihat Winrate Total & Per Map")
        print("4. Lihat Statistik Satu Map")
        print("0. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1" :
            print("TAMBAH RIWAYAT GAME")
            for nomor, m in map_pool.items() :
                print(f"{nomor}. {m}")
            pilihan = input("silahkan pilih nomor map: ")
            if pilihan.isdigit() and int(pilihan) in map_pool:
                nama_map = map_pool[int(pilihan)]
                character = input("masukkan nama character: ")
                kill = input("Kill : ")
                death = input("Death : ")
                assist = input("Assist : ")
                print("1.Menang, 2. Kalah")
                result = input("Menang atau Kalah : ")
                if kill.isdigit() and death.isdigit() and assist.isdigit() and result in ["1" , "2"]:
                    teks_result = "Menang" if result == "1" else "kalah"
                    riwayat.setdefault(nama, [])
                    riwayat[nama].append({
                        "map": nama_map,
                        "character": character,
                        "kill": int(kill),
                        "death": int(death),
                        "assist": int(assist),
                        "result": teks_result
                    })
                    print("riwayat game telah ditambah boskyuuu")
                else :
                    print("INPUT K/D/A YANG BENAR DONG")
            else :
                print("INPUT MAP YANG BENAR DONG")
            input("tekan enter untuk kembali...")
        elif pilih == "2" :
            print(" RIWAYAT GAME MU BOSKYUU")
            nomor_game = 0
            for r in riwayat.get(nama, []):
                nomor_game += 1
                print(f"{nomor_game}. {r['map']}  {r['character']}  K/D/A {r['kill']}/{r['death']}/{r['assist']}  {r['result']}")
            if nomor_game == 0:
                print("Belum ada riwayat game.")
            input("tekan enter untuk kembali...")
        elif pilih == "3":
            total = 0
            menang = 0
            kill_total = 0
            death_total = 0
            assist_total = 0
            for r in riwayat.get(nama, []):
                total += 1
                kill_total += r["kill"]
                death_total += r["death"]
                assist_total += r["assist"]
                if r["result"] == "Menang" :
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
                for m in map_pool.values():
                    t_map = 0
                    w_map = 0
                    for r in riwayat.get(nama, []):
                        if r["map"] == m :
                            t_map += 1
                            if r["result"] ==  "Menang":
                                w_map += 1
                    if t_map == 0:
                        print(f"{m}: belum pernah dimainkan")
                    else :
                        print(f"{m}: {w_map}/{t_map} menang | winrate {w_map / t_map * 100:.1f}%")
            input("tekan enter untuk kembali...")

        elif pilih == "4":
            print("STATISTIK SATU MAP")
            for nomor, m in map_pool.items():
                print(f"{nomor}. {m}")
            pilihan = input("pilih nomor mapnya boskyuuu: ")
            if pilihan.isdigit() and int(pilihan) in map_pool:
                m = map_pool[int(pilihan)]
                t_map = 0
                w_map = 0
                k_map = 0
                d_map = 0
                a_map = 0
                print(f"Statistik map {m}:")
                for r in riwayat.get(nama, []):
                    if r["map"] == m:
                        t_map += 1
                        k_map += r["kill"]
                        d_map += r["death"]
                        a_map += r["assist"]
                        if r["result"] == "Menang":
                            w_map += 1
                        print(f"{r['character']} K/D/A {r['kill']}/{r['death']}/{r['assist']} {r['result']}")
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
        print("  <MENU ADMIN>   login: " + user_ada["username"])
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
            for nomor, m in map_pool.items():
                print(f"{nomor}. {m}")
            input("Tekan Enter untuk kembali...")

        elif pilih == "2" :
            print("TAMBAH MAP BARU")
            nama_map = input("nama map barunya MY BROOOO : ")
            ada = False
            for m in map_pool.values():
                if m.lower() == nama_map.lower():
                    ada = True
            if nama_map == "":
                print("GAK BOLEH KOSONG DONNG")
            elif ada:
                print("MINES LITERASI DONGO")
            else:
                map_pool[len(map_pool) + 1] = nama_map
                print(f"Map {nama_map} berhasil ditambahkan mantap mantap mantap")
            input("tekan Enter untuk kembali...")

        elif pilih == "3":
            print(" GANTI NAMA MAP ")
            for nomor, m in map_pool.items():
                print(f"{nomor}. {m}")
            pilihan = input("Nomor map yang ingin diganti broskkiiiiii : ")
            if pilihan.isdigit() and int(pilihan) in map_pool:
                gx = int(pilihan)
                lama = map_pool[gx]
                baru = input("Nama map pengganti nya bro: ")
                if baru == "":
                    print("GAK BOLEH KOSONG DONG")
                else:
                    map_pool[gx] = baru
                    for daftar_game in riwayat.values():
                        for r in daftar_game:
                            if r["map"] == lama:
                                r["map"] = baru
                    print(f"Map {lama} berhasil diganti dengan {baru}")
            else:
                print("PILIH YANG BENAR DONG ASTAGA")
            input("tekan Enter untuk kembali...")

        elif pilih == "4":
            print(" DAFTAR PENGGUNA ")
            for u in user:
                total = len(riwayat.get(u["username"], []))
                print(f" {u['username']} ({u['role']}) total game: {total}")
            input("Tekan Enter untuk kembali...")

        elif pilih == "5":
            print("SEMUA RIWAYAT GAME ")
            if riwayat == {}:
                print("YAH BELUM ADA YANG MASUKKIN")
            for username, daftar_game in riwayat.items():
                for r in daftar_game:
                    print(f"{username} {r['map']}  {r['character']} K/D/A {r['kill']}/{r['death']}/{r['assist']} {r['result']}")
            input("tekan Enter untuk kembali...")

        elif pilih == "6":
            print(" RESET STATISTIK ")
            print("1. Reset semua pengguna")
            print("2. Reset satu pengguna")
            sub = input("Pilih: ")
            if sub == "1":
                konfirmasi = input("Yakin nih yakin nih hapus semua stat (ya/tidak): ").lower()
                if konfirmasi == "ya":
                    riwayat.clear()
                    print("semua stat berhasil direset. NEW SEASON NEW ME")
                else:
                    print("YAAA GA JADI")
            elif sub == "2":
                target = input("Username yang direset: ").lower()
                konfirmasi = input(f"Yakin reset satu pengguna aja katanya solid parah sih {target}? (ya/tidak): ").lower()
                if konfirmasi == "ya":
                    if target in riwayat:
                        del riwayat[target]
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