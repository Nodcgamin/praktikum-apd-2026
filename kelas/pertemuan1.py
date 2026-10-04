username = "Larry"
password = "068"


while True:
    username_input = input("Masukkan username anda: ").strip()
    password_input = input("Masukkan password anda: ").strip()

    if username_input == username and password_input == password:
        print("Berhasil login")
        break
    elif username_input != username and password_input != password:
        print("Username dan Password salah atau kosong. Coba lagi")
    elif username_input != username:
        print("Username salah")
    else:
        print("Password salah")

darah = {
    'A+': 0, 'A-': 0,
    'B+': 0, 'B-': 0,
    'AB+': 0, 'AB-': 0,
    'O+': 0, 'O-': 0
} 

while True:
    goldar_input = input("Masukkan golongan darah(A/B/AB/O): ").strip().upper()
    if goldar_input not in ['A', 'B', 'AB', 'O']:
        print("Input tidak valid")
        continue

    rh = input("Masukkan Rhesus(+/-): ").strip()
    if rh not in ['+', '-']:
        print("Input tidak valid")
        continue

    jumlah_kantong_darah = input("Masukkan jumlah kantong darah: ").strip()
    if not jumlah_kantong_darah.isdigit() or int(jumlah_kantong_darah) <= 0:
        ("Jumlah kantong darah harus lebih dari 0")
        continue
    jumlah_kantong_darah = int(jumlah_kantong_darah)

    goldar_rh = goldar_input + rh
    darah[goldar_rh] += jumlah_kantong_darah*500

    jawaban = input("Apakah masih mau input lagi? (Y/T): ").strip().upper()
    if jawaban == "T":
        break

print("Ringkasan jumlah darah dalam ml")
for golongan, jumlah in darah.items():
    if jumlah > 0:
        print(f"{golongan}: {jumlah} ml")