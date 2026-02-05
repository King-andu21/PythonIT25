f = open("PythonIT25/files/rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in f:
    vastuvõetud.append(int(rida))

f.close()
print(vastuvõetud)
chosen_year = int(input("Palun sisestage, millise aasta andmeid vajate: "))
index = chosen_year-2011

if index >= len(vastuvõetud):
    print("selle aasta kohta pole andmeid")
else:
    if index > 0:
        print(f"{chosen_year}. aastal oli vastuvõetuid {vastuvõetud[index]}")
    else:
        print("selle aasta kohta pole andmeid")