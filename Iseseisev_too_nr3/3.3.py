fail = open("konto.txt", encoding="UTF-8")
print(fail.read())
for rida in fail:
    if rida > 0:
        print(float(rida))
fail.close()