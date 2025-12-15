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