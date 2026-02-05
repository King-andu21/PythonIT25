def mahlapakkide_arv(ountekogus):
    mahlapakkide_arv = ountekogus * 0.4/3
    mahlapakkide_arv = round(mahlapakkide_arv)
    return mahlapakkide_arv
ountekogus = float(input("sisesta õunte arv kilogrammides: "))
print(mahlapakkide_arv(ountekogus))