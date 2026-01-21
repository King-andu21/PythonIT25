some_list = ["big","weld","hunghorse","bigbonerdownthelane"]
def pikim_sona(lis):
    prev_value = 0
    a = 0
    for i in lis:
        if len(i) > prev_value:
            prev_value = len(i)
            sona = i
        a += 1
    return(sona)
sona= pikim_sona(some_list)
print(f"pikim sõna: {sona}")

def kolm_pikimat_sona(lis):
    for i in lis:
        