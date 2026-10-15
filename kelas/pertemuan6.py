import os
os.system("cls" if os.name == "nt" else "clear")
# kartu = {"merah", "merah", "biru", "hijau"}
# print(kartu)

# matkul = ["apd", "orsikom", "apd", "kalkulus"]
# sks = set(matkul)
# print(sks)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print (angka)

# kelas = {"a", "b", "c"}
# kelas.add("d")
# print(kelas)

# buah = {"apel", "mangga", "jeruk","anggur","kratua"}
# print(buah)
# buah.remove("mangga")
# # print(buah)

# aslab1 = {"1", "2", "3","4","5"}
# aslab2 = {"2", "3", "6","8","10"}
# irisan = aslab1.update(aslab2)
# print(aslab1)

# team = {
# "prx" : "good",
# "LOUD" : "tkzin" ,
# "VITALITY" : "redemption",
# "top_4" : ["LOUD" , "VITALITY"] ,
# }
# # print(F'goood team {team["top_4"]}')
# # print(team.get("prx"))
# # print(team.get("GE"))
# # print(team.get("GE", "Key untuk alamat tidak ada"))
# for i in team.values():
#     print(i)

# for i, j in team.items():
#     print(f"{i} adalah jenis game {j}")

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# # game.update({"wuthering waves" : "better then genshin"})
# # print(game)
# # tambah = game.setdefault("resident evil", "horror")
# # print(game)
# # print("Tipe game", game.setdefault("grow a garden", "gardening"))
# print(len(game))

# game_baru = game.copy()
# game_baru["genshin impact"] = "gacha"
# print(game)
# print(game_baru)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000 , 13000

# menu = dict.fromkeys(key, value)
# print(menu)


menu = {
"ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
"nasi" : ["nasi goreng", "nasi uduk"],
"mie" : ["mie goreng rendang", "mie goreng aceh"],
"kuah" : ["soto", "rawon", "sop iga"]
}
for i, j in menu.items():
    print(f"Kategori {i} memiliki menu :")
    for kategori in j:
        print(kategori)
    print("")




# List_game = dict(Genshin_Impact="Open World", Mole="Moba",
# Stardew_Valley="Farming Simulation")
# print(List_game)
#     print(i)
# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# for i in game.keys():
#     print(i)
# for i in game.keys():
#     print(i)