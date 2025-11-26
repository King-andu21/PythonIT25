#---o---

# 1. Vanusepiiranguga üritus

#---o---
vanus = 0
# vanus = int(input("Sisesta oma vanus: "))
if vanus >= 18:
    print("Sissepääs lubatud")
else:
    print("Jookse minema tatt")
#---o---

# 2. Ilmaennustuse rakendus (and)

#---o---
temp = 0
try:
    # temp = int(input("Sisesta temperatuur kraadides: "))
    if temp < 0:
        print("Kanna talveriideid")
    elif temp >= 0 and temp <= 15:
        print("Kanna kevad-sügis rõivaid")
    else:
        print("Kanna suveriideid")
except: 
    print("EROOR, Sisesta täisarv")

#---o---

# 3. Matemaatika Test (randint)

#---o---
#---o---

# 4. Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)

#---o---
import random
mynt = random.randint(0,1)
try:
    guess = int(input("Kumb pool tuleb? (kiri või kull) 0/1: "))
    if guess == 0:
        guess_t = "kiri"
    else:
        guess_t = "kull"
    if mynt == 0:
        tulemus = "kiri"
    else:
        tulemus = "kull"
    if guess == mynt:
        print(f"Võit, {tulemus} tuli")
    else:
        print(f"Kaotus, tuli: {tulemus}")
    print(f"arvamus:{guess_t}")
    print(f"tulemus:{tulemus}")
except:
    print("sisesta kiri (0) või kull (1)")