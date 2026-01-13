# 1.
for i in range(21):
    print(i)
# 2.
import random
for i in range(20):
    print(random.randint(1,99))
# 3.
some_list = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
even_list = []
uneven_list = []
for x in range(len(some_list)):
    
    if some_list[x] % 2 == 0:
        even_list.append(some_list[x])
    else:
        uneven_list.append(some_list[x])
print(f"Paaris: {even_list} :) ")
print(f"Paaritu: {uneven_list} :( ")
# 4.
for i in range(1,43):
    print(i)
    if i%3==0 and i%5==0:
        print("TIKTAK")
    elif i%3==0:
        print("TIK")
    else:
        print("TAK")
# 6.
nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
clean_list = []
for i in nimed:
    if i not in clean_list:
        clean_list.append(i)
    
print(clean_list)

# 8.
for i in range(11):
    print(f"{i} * {i} = {i*i}")

# 9.
# list = ["+","-","*","/","^"]
# for _ in range (10):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     tehe = random.choice(list)
#     if tehe=="+":
#         print(f"{arv1}{tehe}{arv2} = {arv1 + arv2}")
#     if tehe=="-":
#         print(f"{arv1}{tehe}{arv2} = {arv1 - arv2}")
#     if tehe=="*":
#         print(f"{arv1}{tehe}{arv2} = {arv1 * arv2}")
#     if tehe=="/":
#         print(f"{arv1}{tehe}{arv2} = {arv1 / arv2}")
#     if tehe=="^":
#         print(f"{arv1}{tehe}{arv2} = {arv1 ^ arv2}")



# 10.
# hinne = 0
# list = ["+","-","*","/"]
# kysimuste_arv = 10
# for _ in range (kysimuste_arv):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     tehe = random.choice(list)
#     if tehe=="+":
#         print(f"{arv1}{tehe}{arv2} = ")
#         vastus = arv1 + arv2
#         sisestatud_vastus = int(input("mis on vastus?: "))
#         if vastus == sisestatud_vastus:
#             hinne += 1 
#         else:
#             print(f"vastus oli {vastus}")
#     if tehe=="-":
#         print(f"{arv1}{tehe}{arv2} = ")
#         vastus = arv1 - arv2
#         sisestatud_vastus = int(input("mis on vastus?: "))
#         if vastus == sisestatud_vastus:
#             hinne += 1 
#         else:
#             print(f"vastus oli {vastus}")
#     if tehe=="*":
#         print(f"{arv1}{tehe}{arv2} = ")
#         vastus = round((arv1 * arv2),1)
#         sisestatud_vastus = int(input("mis on vastus?: "))
#         if vastus == sisestatud_vastus:
#             hinne += 1 
#         else:
#             print(f"vastus oli {vastus}")
#     if tehe=="/":
#         print(f"{arv1}{tehe}{arv2} = ")
#         vastus = round((arv1 / arv2),1)
#         sisestatud_vastus = float(input("mis on vastus?: "))
#         if vastus == sisestatud_vastus:
#             hinne += 1 
#         else:
#             print(f"vastus oli {vastus}")

# print(f"punktid kokku {hinne} {hinne/kysimuste_arv*10}%")
# if hinne/kysimuste_arv >= 0.5:
#     print("A")
# else: 
#     print("MA")

# 11.

# #1
# arv = 5
# for i in range(1,6):
#     print(" " * i+ "*" * arv)
#     arv -=1
# #2
# arv = 5
# for i in range(1,6):
#     print("*" * arv)
#     arv -= 1
# #3
# arv = 5
# for i in range(1,6):
#     print(" " * arv+ "*" * i)
#     arv -=1
# #4
# for i in range(1,6):
#     print("*" * i)

# 12.
sum_list = []
selector = 0
even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]
for i in even_nums:
    if i % 2 == 0:
        sum_list.append(i)
    else:
        break
print (f"kokku: {sum(sum_list)}")

# 13.
a = 0
keskmine_range = 0
keskmine_hind = 0
ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]
for i in ev_data:
    a += 1
    print(f"{i[0]:26} \033[1;30;42m{i[1]:6} \033[1;30;43m{i[2]:8}\033[0m")
    if a >= 2:
        keskmine_range += int(i[1])
        keskmine_hind += int(i[2])
keskmine_range = round(keskmine_range/a)
keskmine_hind = round(keskmine_hind/a)
print(f"\033[0;32;40m keskmine range on: \033[1;30;42m{keskmine_range}, \033[0;32;40mKeskmine hind on: \033[1;30;43m{keskmine_hind} \033[0m")
