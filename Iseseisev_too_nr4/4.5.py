chosen_file = input("Sisesta failinimi: ")
f = open(f"PythonIT25/files/{chosen_file}" , encoding="UTF-8")
def pronksikarva_summa():
    value = 0
    for i in f:
        i = int(i)
        if i == 1:
            value += 1
        if i == 2:
            value += 2
        if i == 5:
            value += 5
    return value
print(pronksikarva_summa())