

#batas = 10
#for i in range(batas):
#    print("Perulangan ke-", i)

#game = ["Genshin", 7.0, True]
#for i in game:
    #print(i)


#for i in range (1,10,1) :
   # print(i)

#for i in range(1, 8):# Mengontrol baris dalam tabel perkalian
   ## for j in range(1, 10):# Mengontrol kolom dalam tabel perkalian
       # print(f'{i} x {j} = {i * j}')
#print('')       




#n = int(input("masukkan nilai"))
#hitung = 0
#for i in range (1,n) :
   
    #if i % 2 != 0 :
        #hitung += 1
        #print(i)
# print(f"total ganjil adalah  {hitung}")




for i in range(30):
    if i < 10:
        break
    print(i)    


angka_benar = 6

while True:
    print("==== game tebak angka ====")

    angka_input = int(input("masukkan angka 1-10 : "))

    if angka_benar == angka_input :
        print("angka yang kamu massukan benar")
        break
    elif angka_input >= 11 :
        print("sdm rendah homeless aids miskin asu orang cuma 1 - 10 dasar tolol")
    else :
        print("salah silahkan tebak lagi")