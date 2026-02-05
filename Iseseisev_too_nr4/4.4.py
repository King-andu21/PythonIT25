def tervitus(kulaliste_arv):
    for i in range(int(kulaliste_arv)):
        print("Võõrustaja 'Tere!'")
        print(f"Täna {i+1}. kord tervitada, mõtiskleb võõrustaja.")
        print("Tere, suur tänu kutse eest!")
orjade_arv = input("sisesta orjade arv: ")

tervitus(orjade_arv)