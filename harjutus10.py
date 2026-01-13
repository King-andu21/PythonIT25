

import statistics
list = []
while True:
    a = input("Sisesta arv: ")
    if str(a) == "":
        break
    print(f"entered {a}")
    list.append(a)
print(f"the list you made: {list}")
print(f"average from your list: {statistics.mean(list)}")