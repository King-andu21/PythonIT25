def ringid(ringide_arv):
    reward = 0
    ringid = 1
    for i in range(ringide_arv):
        if ringid % 2 == 0:
            reward += ringid
        ringid += 1
    return(reward)
ringide_arv = int(input("Sisestage ringide arv: "))
print(f"Saadavate porgandite koguarv on {ringid(ringide_arv)}.")