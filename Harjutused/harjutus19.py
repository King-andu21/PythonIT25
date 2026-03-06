import json
opilasi_12 = 0
opilasi_11 = 0
opilasi_10 = 0
# Faili avamine ja JSON-i laadimine
with open('PythonIT25/harjutus19_files/haridustulemused.json', 'r', encoding='utf-8') as file:
    tulemused = json.load(file)

for tul in tulemused:
    if tul["klass"] == "12":
        print(tul["nimi"])
        for teg in tul["tegevused"]: 
            print(" ",teg)
        print("----------")
        for y in tul["hinded"]:
            print(y,":", tul["hinded"][y]) 
        print("___________")
        opilasi_12 += 1
    if tul["klass"] == "11":
        opilasi_11 += 1
    if tul["klass"] == "10":
        opilasi_10 += 1

print(opilasi_12, opilasi_11, opilasi_10)