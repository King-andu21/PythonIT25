chosen_file = input("Sisesta failinimi: ")
f = open(chosen_file, encoding="UTF-8")
for rida in f:
    jark += 1
    print(f"{jark}{rida}")
chosen_song = int(input("Valige laulu järjekorranumber: "))
print(f[chosen_song])
f.close()