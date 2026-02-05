import os
print(os.listdir('PythonIT25/files/muusika'))
chosen_file = input("Sisesta failinimi: ")
f = open(f"PythonIT25/files/muusika/{chosen_file}", encoding="UTF-8")
jark = 0
for rida in f:
    print(f"{jark}. {rida}")
    jark += 1
chosen_song = int(input("Valige laulu järjekorranumber: "))

jark = 0
f = open(f"PythonIT25/files/muusika/{chosen_file}", encoding="UTF-8")
for rida in f:
    if chosen_song == jark:
        print(f"{jark}. {rida}")
    jark += 1
f.close()