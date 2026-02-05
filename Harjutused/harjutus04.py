#---o---

# 1. Aia pikkus

#---o---
a = float(input ("sisesta arv 1 (meetrites): "))
b = float(input ("sisesta arv 2 (meetrites): "))
c = a*2+b*2
print(f"aia kogupikkus on  {c} meetrit")
#---o---

# 2. Raamatute allahindlus

#---o---
alla_hindlus= 0.3
tava_hind= 12.53
raamatute_arv = int(input("sisesta raamtute soovitud kogus: "))
summa = raamatute_arv*(tava_hind-(tava_hind*alla_hindlus))
print(f"{raamatute_arv} raamatu hind soodustusega on {summa:.2f}€.")
#---o---

# 4. Kingituste pakkimine

#---o---
karbi_maht = 5
kingituste_arv = int(input("kingituste arv: "))
tais = kingituste_arv//karbi_maht
yle = kingituste_arv%karbi_maht
print(f"saab teha {tais} täis kinkekasti. üle jääb {yle} kingitusts.")
