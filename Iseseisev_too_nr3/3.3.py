fail = open("Python_IT25_Uus/files/konto.txt", encoding="UTF-8")
for rida in fail:
    if float(rida) > 0:
        print(float(rida))
fail.close()