import csv

faili_nimi = "PythonIT25/harjutus18_files/EstonianBasketballGames.csv"
tiim_list = []
x= 0
with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)
    for rida in csv_lugeja:
        print(rida)
        if rida[1] not in tiim_list:
            print(rida[1])
            x += 1
            tiim_list.append(rida[1])
        if rida[2] not in tiim_list:
            print(rida[2])
            x += 1
            tiim_list.append(rida[2])
    print(len(tiim_list)-2)
print(tiim_list)