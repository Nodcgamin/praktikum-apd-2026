import os
user = [{"username": "bos", "password": "gamin", "role": "admin"}]  
map_pool = {1: "dread", 2: "kreaster", 3: "kitres", 4: "bortologo"}  
riwayat = {}                                                          
user_ada = None     

def kembali():
    input("tekan enter untuk kembali")

def tampilkan_map_pool():
    for nomor,m in map_pool.items():
        print(f"{nomor}. {m}")

def tampilkan_riwayat(nama):
    nomor_game = 0
    for r in riwayat.get(nama,[]):
        nomor_game += 1
        print(f"{nomor_game}. {r['map']}  {r['character']}  K/D/A {r['kill']}/{r['death']}/{r['assist']}  {r['result']}")
    if nomor_game == 0 :
        print("main dulu dong ahhhhhdhadhahdahdash")
        

def total_semua_game():
    total = 0
    for daftar in riwayat.values():
        total += len(daftar)
    return total

def daftar_nama_map():
    hasil = []
    for m in map_pool.values():
        hasil.append(m)
    return hasil

def hitung_winrate(menang , total):
    if total == 0:
        return 0
    return menang / total * 100 

def username_tersedia(username_baru):
    for u in user:
        if u["username"] == username_baru:
            return False
    return True

def input_angka(pesan):
    while True:
        try :
            nilai = int(input(pesan))
            if nilai < 0:
                raise ValueError("kok bisa negatif sih astagaaaaaaaaa")
        except ValueError:
            print("woy kok kosong kaya hidup lu")
        else:
            return nilai
        
def hitung_statistik(daftar):
    hasil = {"total": len(daftar), "menang": 0, "kill": 0, "death": 0, "assist": 0} 
    for r in daftar:
        hasil["kill"] += r["kill"]
        hasil["death"] += r["death"]
        hasil["assist"] += r["assist"]
        if r["result"] == "Menang":
            hasil["menang"] += 1
    return hasil

def cetak_game(r, awalan=""):
    print(f"{awalan}{r['map']}  {r['character']}  K/D/A {r['kill']}/{r['death']}/{r['assist']}  {r['result']}")

def cetak_ringkasan(s):
    print(f"total game : {s['total']}menang : {s['menang']}kalah : {s['total'] - s['menang']}")
    print(f"winrate    : {hitung_winrate(s['menang'], s['total']):.0f}%")
    print(f"total K/D/A: {s['kill']}/{s['death']}/{s['assist']}")

def proses_login():
    akun = None
    username = input("masukkan nama: ").lower()
    password = input("massukan password:")
    for u in user:
        if u["username"] == username and u["password"] == password:
            akun = u
    if akun is None:
        print("username atau password salah yang benar dong")
        kembali()
    return akun

def proses_register():
    print("Regis Bos Ku")
    username = input("Masukkan Username:").lower()
    password = input("Masukkan Password:")
    try:
        if username == "" or password == "":
            raise ValueError("masukkan username dan password tidak boleh kosong tolol")
        if not username_tersedia(username):
            raise ValueError("yah sudah ke ambil")
    except ValueError as e:
        print(e)
    else:
        user.append({"username": username, "password": password, "role": "user"})
        print("Mantap silahkan Login")
    finally:
        kembali()


def menu_login():
    akun = None  # lokal
    print("Sistem Pencatatan game\n1. login\n2. register \n3. logout")
    pilih = input("silahkan pilih menu:")
    if pilih == "1":
        akun = proses_login()
    elif pilih == "2":
        proses_register()
    elif pilih == "3":
        print("tamatlah sudah cerita kami")
        akun = "selesai"
    else:
        print("pilih yang benar dong")
        kembali()
    return akun

def user_tambah_riwayat(nama):
    print("TAMBAH RIWAYAT GAME")
    tampilkan_map_pool()
    pilihan = input_angka("silahkan pilih nomor map: ")
    try:
        nama_map = map_pool[pilihan]
    except KeyError:
        print("INPUT MAP YANG BENAR DONG")
    else:
        character = input("masukkan nama character: ")
        kill = input_angka("Kill : ")
        death = input_angka("Death : ")
        assist = input_angka("Assist : ")
        print("1.Menang, 2. Kalah")
        result = input_angka("Menang atau Kalah : ")
        if result in [1, 2]:
            riwayat.setdefault(nama, []).append({
                "map": nama_map, "character": character, "kill": kill, "death": death,
                "assist": assist, "result": "Menang" if result == 1 else "kalah"
            })
            print("riwayat game telah ditambah boskyuuu")
        else:
            print("INPUT MENANG ATAU KALAH YANG BENAR DONG")
    finally:
        kembali()

def user_lihat_riwayat(nama):
    print(" RIWAYAT GAME MU BOSKYUU")
    tampilkan_riwayat(nama)
    kembali()


def user_statistik_total(nama):
    daftar = riwayat.get(nama, [])  
    print("STATISTIK TOTAL")
    if len(daftar) == 0:
        print("Belum ada data game.")
    else:
        cetak_ringkasan(hitung_statistik(daftar))
        print("WINRATE PER MAP")
        for m in daftar_nama_map():
            s = hitung_statistik([r for r in daftar if r["map"] == m])  
            if s["total"] == 0:
                print(f"{m}: belum pernah dimainkan")
            else:
                print(f"{m}: {s['menang']}/{s['total']} menang | winrate {hitung_winrate(s['menang'], s['total']):.0f}%")
    kembali()


def user_statistik_map(nama):
    print("STATISTIK SATU MAP")
    tampilkan_map_pool()
    pilihan = input_angka("pilih nomor mapnya boskyuuu: ")
    try:
        m = map_pool[pilihan]
    except KeyError:
        print("Nomor map tidak valid!")
    else:
        daftar = [r for r in riwayat.get(nama, []) if r["map"] == m]  
        print(f"Statistik map {m}:")
        for r in daftar:
            cetak_game(r)
        if len(daftar) == 0:
            print("Belum ada game di map ini.")
        else:
            print()
            cetak_ringkasan(hitung_statistik(daftar))
    finally:
        kembali()

def admin_lihat_map():
    print("MAP POOL SAAT INI")
    tampilkan_map_pool()
    kembali()

def admin_tambah_map():
    print("TAMBAH MAP BARU")
    nama_map = input("nama map barunya MY BROOOO : ")
    try:
        if nama_map == "":
            raise ValueError("GAK BOLEH KOSONG DONNG")
        if nama_map.lower() in [m.lower() for m in daftar_nama_map()]:
            raise ValueError("MINES LITERASI DONGO")
    except ValueError as e:
        print(e)
    else:
        map_pool[len(map_pool) + 1] = nama_map
        print(f"Map {nama_map} berhasil ditambahkan mantap mantap mantap")
    finally:
        kembali()

def admin_ganti_nama_map():
    print(" GANTI NAMA MAP ")
    tampilkan_map_pool()
    pilihan = input_angka("Nomor map yang ingin diganti broskkiiiiii : ")
    try:
        lama = map_pool[pilihan]
    except KeyError:
        print("PILIH YANG BENAR DONG ASTAGA")
    else:
        baru = input("Nama map pengganti nya bro: ")
        if baru == "":
            print("GAK BOLEH KOSONG DONG")
        else:
            map_pool[pilihan] = baru
            for daftar_game in riwayat.values():
                for r in daftar_game:
                    if r["map"] == lama:
                        r["map"] = baru
            print(f"Map {lama} berhasil diganti dengan {baru}")
    finally:
        kembali()

def admin_daftar_pengguna():
    print(" DAFTAR PENGGUNA ")
    for u in user:
        print(f" {u['username']} ({u['role']}) total game: {len(riwayat.get(u['username'], []))}")
    print(f"Total semua game: {total_semua_game()}")
    kembali()

def admin_semua_riwayat():
    print("SEMUA RIWAYAT GAME ")
    if riwayat == {}:
        print("YAH BELUM ADA YANG MASUKKIN")
    for username, daftar_game in riwayat.items():
        for r in daftar_game:
            cetak_game(r, f"{username} ")
    kembali()

def admin_reset_statistik():
    print(" RESET STATISTIK 1. reset semua pengguna 2. reset satu pengguna")
    pengganti = input("Pilih: ")
    if pengganti == "1":
        konfirmasi = input("Yakin nih yakin nih hapus semua stat (ya/tidak): ").lower()
        if konfirmasi == "ya":
            riwayat.clear()
            print("semua stat berhasil direset. NEW SEASON NEW ME")
        else:
            print("YAAA GA JADI")
    elif pengganti == "2":
        target = input("Username yang direset: ").lower()
        konfirmasi = input(f"Yakin reset satu pengguna aja katanya solid parah sih {target}? (ya/tidak): ").lower()
        if konfirmasi == "ya":
            try:
                del riwayat[target]
            except KeyError:
                print(f"{target} belum punya statistik.")
            else:
                print(f"Statistik {target} berhasil direset.")
        else:
            print("YAAA GA JADI")
    else:
        print("PILIH YANG BENAR DONG MIN")
    kembali()

def menu_user(akun):
    nama = akun["username"]  # lokal
    print(" Menu login sebagai = " + nama)
    print("1. Tambah Riwayat Game\n2. Lihat Riwayat Game Saya\n3. Lihat Winrate Total & Per Map")
    print("4. Lihat Statistik Satu Map\n0. Logout")
    pilih = input("Pilih menu: ")
    if pilih == "1":
        user_tambah_riwayat(nama)
    elif pilih == "2":
        user_lihat_riwayat(nama)
    elif pilih == "3":
        user_statistik_total(nama)
    elif pilih == "4":
        user_statistik_map(nama)
    elif pilih == "0":
        akun = None
    else:
        print("Menu tidak valid!")
        kembali()
    return akun

def menu_admin(akun):
    print("  <MENU ADMIN>   login: " + akun["username"])
    print("1. Lihat Map Pool\n2. Tambah Map Baru\n3. Ganti Nama Map\n4. Lihat Daftar Pengguna")
    print("5. Lihat Semua Riwayat Game\n6. Reset Statistik (Season Baru)\n0. Logout")
    pilih = input("Pilih menu: ")
    if pilih == "1":
        admin_lihat_map()
    elif pilih == "2":
        admin_tambah_map()
    elif pilih == "3":
        admin_ganti_nama_map()
    elif pilih == "4":
        admin_daftar_pengguna()
    elif pilih == "5":
        admin_semua_riwayat()
    elif pilih == "6":
        admin_reset_statistik()
    elif pilih == "0":
        akun = None
    else:
        print("PILIH YANG BENAR DONG ASTAGA")
        kembali()
    return akun

if __name__ == "__main__":
    berjalan = True
    while berjalan:
        os.system("cls" if os.name == "nt" else "clear")
        if user_ada is None:
            hasil = menu_login()
            if hasil == "selesai":
                berjalan = False
            else:
                user_ada = hasil
        elif user_ada["role"] == "user":
            user_ada = menu_user(user_ada)
        else:
            user_ada = menu_admin(user_ada)