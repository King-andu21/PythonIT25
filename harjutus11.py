def my_boner(a, b):
    c = a + b
    return c
    print("Tere Peter Griffin")
print(my_boner(2, 3))
some_list = ["big","weld","hunghorse","bigbonerdownthelane","longhorseee"]

def pikim_sona(lis):
    prev_value = 0
    sona = ""
    for i in lis:
        if len(i) > prev_value:
            prev_value = len(i)
            sona = i
    return(sona)

sona= pikim_sona(some_list)
print(f"pikim sõna: {sona}")

def length(e):
        return len(e)

def kolm_pikimat_sona(lis):
    if len(lis) > 2:
        lis.sort(key=length, reverse=True)
    return(lis[0:3])
print(kolm_pikimat_sona(some_list))