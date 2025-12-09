# Loo muutuja, mis sisaldab kuulsat tsitaati. Koosta uus string, mis sisaldab tsitaati koos autori
# nimega. Kasuta selleks erinevaid jutumärke: näiteks tsitaat ühekordsete jutumärkidega ja kogu
# lause topeltjutumärkidega või vastupidi. Veendu, et vormistus on korrektne ja tsitaat on selgelt
# eristatud.
tsitaat = 'William Randolph Hearst "Piisavalt suur pealkiri teeb iga uudise suureks."'
print (tsitaat)
# ---o---
# 3.
# ---o---
# eesnimi = "Jüri"
# perenimi = "Jurakas"
# initials = f"{eesnimi[0]}.{perenimi[0]}."
# print(initials)
# ---o---
# 6.
# ---o---
andmerida = "1,Marshal,Martinovic,mmartinovic0@dedecms.com,Male,40.19.226.175"
ar_s = andmerida.split(",") 
print(ar_s)
print(ar_s[2],ar_s[3],ar_s[5])

# ---o---
# 8.
# ---o---
posts = 137
lk_max = 10
jaak = posts // lk_max
viimane_leht = posts % lk_max
if viimane_leht > 0:
    jaak +=1
print(f"mitu lehte vaja:{jaak}, viimases lehes postitused:{viimane_leht}")

# ---o---
# 10.
# ---o---
som_list = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede"]
print(som_list[2],som_list[3])
print(len(som_list))
som_list.append("Laupäev")
som_list.append("Pühapäev")
print(len(som_list),som_list)
som_list.sort(reverse=True)
print(som_list[-1])
# ---o---
# 12.
# ---o---
tulemused = [["Alice", 25, [10.2, 9.8, 10.5]],
["Bob", 22, [9.5, 9.6, 9.7]],
["Charlie", 28, [11.1, 11.2, 11.5]]]
for x in tulemused:
    x[2].sort()
    print (x[0], x[2][-1])
#   print (max(x[2]))
# ---o---
# 14.
# ---o---
vanus = int(input("Mis on su vanus: "))
piletityyp = "soodus"
if piletityyp == "tais":
    if vanus < 18:
        hind = 10
    elif vanus <= 64:
        hind = 20
    else:
        hind = 15
if piletityyp == "soodus":
    if vanus < 18:
        hind = 8
    elif vanus <= 64:
        hind = 15
    else:
        hind = 8
print(f"{piletityyp}pileti hind on {hind}€")
# ---o---
# 16. Temperatuurid
# ---o---
temps = [[5, 8, 12, 10, 7, 9, 11, 14, 16, 13, 10, 6, 4, 3, 2, 4, 6, 8, 10, 12, 15,
17, 18, 16, 13, 10],
[1, 4, 6, 7, 9, 11, 13, 15, 12, 9, 7, 5, 3, 2, 3, 6, 8, 10, 12, 15, 17, 19,
18, 16, 13, 11],
[8, 10, 13, 15, 16, 18, 19, 20, 17, 15, 13, 11, 10, 9, 8, 10, 12, 14, 16,
18, 20, 22, 21, 18, 16, 14],
[2, 5, 7, 9, 12, 15, 17, 18, 15, 13, 11, 8, 6, 5, 4, 7, 9, 12, 14, 16, 19,
21, 20, 18, 16, 13],
[6, 8, 11, 14, 16, 18, 20, 21, 18, 15, 12, 10, 8, 6, 5, 8, 10, 13, 15, 18,
20, 22, 21, 19, 16, 13],
[11, 14, 17, 19, 21, 23, 24, 22, 19, 16, 13, 11, 10, 9, 9, 12, 15, 18, 20,
23, 25, 27, 26, 24, 21, 18],
[9, 11, 14, 16, 18, 20, 22, 21, 18, 16, 13, 11, 9, 8, 7, 10, 13, 16, 18,
21, 23, 24, 23, 21, 18, 15],
[7, 10, 13, 15, 17, 20, 22, 23, 20, 17, 14, 12, 10, 9, 8, 11, 14, 17, 19,
22, 24, 26, 25, 23, 20, 17],
[3, 6, 9, 11, 13, 15, 17, 18, 16, 14, 11, 9, 7, 6, 5, 8, 10, 13, 15, 17,
19, 21, 20, 18, 15, 12],
[1, 3, 5, 7, 9, 11, 13, 15, 12, 9, 7, 5, 3, 2, 3, 6, 8, 10, 12, 15, 17, 19,
18, 16, 13, 11],
[6, 8, 11, 14, 16, 18, 20, 21, 18, 15, 12, 10, 8, 6, 5, 8, 10, 13, 15, 18,
20, 22, 21, 19, 16, 13],
[10, 13, 16, 18, 20, 22, 23, 24, 21, 18, 15, 13, 11, 10, 9, 12, 15, 18, 20,
23, 25, 27, 26, 24, 21, 18]]