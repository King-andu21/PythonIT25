chosen_file = input("vali fail kust nimed valitakse: ")
f = open(f"Python_IT25_Uus/files/{chosen_file}", encoding="UTF-8")
jark = 1
from datetime import *
for i in f:
    if datetime.now().day == jark:
        print(f"vastama tuleb: {jark}. {i}")
    jark += 1