#---o---
# Tervitus
#---o---
print("Tere, maailm!")
#---o---
# Aasta liblikas
#---o---
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = f"{aasta}{lause_keskosa}{liblikas}"
print(f"{lause}")
#---o---
# Pilved
#---o---
korgus = 0
# korgus = float(input("Sisesta pilvede kõrgus kilomeetrites: "))
if korgus <= 6:
    print("Need ei ole ülemised pilved")
elif korgus > 6:
    print("Need on ülemised pilved")
#---o---
# Bussid
#---o---
inimesed_arv = int(input("Sisesta transporditavade inimeste arvu: "))
buss_kohad = int(input("Sisesta ühe bussi kohtade arvu: "))
viimase_buss_inimesed = inimesed_arv % buss_kohad
buss_vaja =  inimesed_arv // buss_kohad
print(f"Täis Busse: {buss_vaja}")
if viimase_buss_inimesed > 0:
    buss_vaja = buss_vaja+1
print(f"Busse vaja: {buss_vaja}")
if inimesed_arv > buss_kohad:
    print(f"Viimases bussis inimesi: {viimase_buss_inimesed}")