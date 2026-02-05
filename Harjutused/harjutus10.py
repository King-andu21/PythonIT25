

# import statistics
# list = []
# while True:
#     a = input("Sisesta arv: ")
#     if str(a) == "":
#         break
#     print(f"entered {a}")
#     list.append(a)
# print(f"the list you made: {list}")
# print(f"average from your list: {statistics.mean(list)}")

# 2.
import random
tulemused = []
a = random.randint(1,10)
katsed = 0
while True:
    vastus = int(input("arva number:"))
    katsed += 1
    if vastus == a:
        print(f"Õige! Oled Karin Eegereid, sul võtis \033[1;32;40m{katsed} katset\033[0m,  et ära arvata")
        again = input(f"Tahad uuesti mängida? y/n: ")
        if again == "y":
            tulemused.append(katsed)
            a = random.randint(1,10)
            katsed = 0
        else:
            tulemused.append(katsed)
            print(f"Aitäh mängimise eest!")
            print(f"sinu tulemused {tulemused}")
            break
    else:
        print("Proovi uuesti Karin Eegereid")