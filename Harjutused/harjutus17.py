import os
try:
    os.mkdir(f"PythonIT25/harjutus17_files")
except:
    print(f"harjutus17_files eksisteerib")
mehed_kokku = 0
naised_kokku = 0
mehed_tootunnid_kokku = 0
mehed_palk = 0

# fail = open("PythonIT25/harjutus17_files/palgad.txt", encoding="UTF-8")
with open("PythonIT25/harjutus17_files/palgad.txt", encoding="UTF-8") as fail:
    rida = fail.readlines()
    for i in rida: 
        cut = i.split(",")
        print(cut)
        if cut[3] == "Mees":
            mehed_kokku += 1
        else:
            naised_kokku += 1


    
print(f"mehed kokku: {mehed_kokku}")
print(f"Naised kokku: {naised_kokku}")

