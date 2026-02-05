soogi_hind = 10
ruumi_rent = 55
kutsutud_inimesed = int(input("mitu inimest on kutsutud: "))
tulevad_inimesed = int(input("mitu inimest tuleb: "))
def eelarve(kutsutud_inimesed,tulevad_inimesed):
    eelarve_max = kutsutud_inimesed*soogi_hind+ruumi_rent
    eelarve_min = tulevad_inimesed*soogi_hind+ruumi_rent
    return eelarve_max,eelarve_min
maksimaalne_eelarve = eelarve(kutsutud_inimesed,tulevad_inimesed)[0]
minimaalne_eelarve = eelarve(kutsutud_inimesed,tulevad_inimesed)[1]
print(f"Maksimaalne eelarve: {maksimaalne_eelarve}")
print(f"Maksimaalne eelarve: {minimaalne_eelarve}")