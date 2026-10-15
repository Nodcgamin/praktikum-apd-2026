# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# print(formula1[3])
# print(formula1[4][1])

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)

# sirkuit.append("Spa-Francorchamps")
# print(sirkuit)

# sirkuit.extend(["Spa-Francorchamps", "Interlagos"])
# print(sirkuit)
# sirkuit.insert(3, "Interlagos")
# print(sirkuit)

# sirkuit[3] = "Monza Italia"
# print(sirkuit)

# sirkuit[0:3] = ["bahrain", "monggol" , "singapore"]
# print(sirkuit)


# del sirkuit[4]
# print(sirkuit)

# sirkuit.remove("singapore")
# print(sirkuit)

# ambil_sirkuit = sirkuit.pop(2)
# print(ambil_sirkuit)

# print(sirkuit[0:4:2])

# team1 = ["Mercedes", "Ferrari", "MacLaren"]
# team2 = ["Red Bull", "Alpine", "Aston Martin"]
# gabung_team = team1 + team2
# print(gabung_team)

# juara_WDC = ["MacLaren", "Red Bull"]
# juara = juara_WDC * 10
# print(juara)
# print(juara_WDC)

# cool = [
#     ["Red bull, verstappen",3],
#     ["ferrari","lecler", 16],
#     ["mercedes", "kimi", 20],
#     ["mclaren", "norris",1],
# ]
# print(cool[3][0])

# for i in cool:
#     for j in i:
#         print(j,)


# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# print(chara)
# print(chara[2])
# print(chara[-1])
# print(chara[4][0])

# listchara = list(chara)
# # listchara.append("Yui ")

# chara = tuple(listchara)
# print(chara)

# # listchara.append(chara_baru)
# # chara = tuple(listchara)
# # print(chara)
# listchara = list(chara)

# del listchara[3]
# chara = tuple(listchara)
# print(chara)
chara = ("Yukari", "Yukino", "Odette", "Senku")
(Persona, Oregairu, *anime) = chara
umur = (20, 22, 25, 17)
print(Persona)
print(anime)
join = chara + umur
print(join)



