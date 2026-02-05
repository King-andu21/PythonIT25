#---o---
# Harjutus 7.1
#---o---
playlist = [ '"1. ALIKA  "Bridges"',
             '2. Anett x Fredi  "Read Between The Lines"', 
             '3. villemdrillem  "leekiv armastus"', 
             '4. Clicherik & Mäx  "PAKSUD"', 
             '5. nublu  "ära ärata"', 
             '6. NOËP  "Move Your Feet"', 
             '7. Trad.Attack!  "Bring It On"', 
             '8. Bedwetters  "It Is What It Is"', 
             '9. Reket  "Panama paberid"', 
             '10. Grete Paia  "Võluväel"']
print(playlist)
# lugu = int(input("Millist lugu tahad kuulata?: "))
# print(f"kohe hakkab nängima lugu {playlist[lugu-1]}")

#---o---
# Harjutus 7.2
#---o---
mootmised = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]
print(f"mõõtetav kuu {mootmised[0]}")
print(f"Viimane mõõdetav tulemus: {mootmised[-1]} kraadi")
print(f"Temperatuurid {mootmised[1:-1]}")
print(f"Max temp {max(mootmised[1:-1])}, Min temp {min(mootmised[1:-1])}")
kogus = len(mootmised[1:-1])
sum = sum(mootmised[1:-1])
print(f"Keskmine Temp {sum/kogus}")
count = mootmised.count(-20)
print(f"-20 kraadi esineb {count} korda")
del mootmised[4]
print(f"Temperatuurid {mootmised[1:-1]}")
mootmised.insert(4,16)
jark = mootmised[1:-1]
print(jark)
print (jark.sort())