# ---o---
# 1.
# ---o---
def temp_converter(temp,conversion):
    # Temp (int)- Temperatuur
    # Conversion (str)- Teisendamise tüüp

    # Kui teisendamise tüüp on celsius fahrenheitiks siis kasuta valemit "temp*9/5+32"
    # ja tagasta saadud arv.
    if conversion == "C" or conversion == "c":
        converted_temp = temp*9/5+32
        return converted_temp
    # Kui teisendamise tüüp on fahrenheiti celsiuseks siis kasuta valemit "(temp-32)*5/9"
    # ja tagasta saadud arv.
    if conversion == "F" or conversion == "f":
        converted_temp = (temp-32)*5/9
        return converted_temp
    # Kui teisandamise tüüp pole eelnevate seas tagasta veateade.
    else:
        return("Vale teisendamise tüüp")

# Kasutaja valib teisendamise tüübi.
conversion_type = input("Vali teisendamise tüüp (C-Celsius Fahrenheitiks, F-Fahrenheit Celsiuseks): ")
# Kasutaja valib temperatuuri väärtuse.
temperature = int(input("Vali temperatuur: "))
# Prindi valmis arvutatud väärtus kasutadas "temperature" ja "conversion_type" väärtuseid.
print(temp_converter(temperature,conversion_type))

# ---o---
# 2.
# ---o---

print ((lambda kytusekulu,vahemaa: (kytusekulu / 100) * vahemaa)(5,150))

# ---o---
# 3.
# ---o---
def bank(algne_saldo,toiming,summa):
    if toiming == "deposiit":
        uus_saldo = algne_saldo+summa
        return uus_saldo
    if toiming == "väljavõte":
        uus_saldo = algne_saldo-summa
        return uus_saldo
    else:
        return "vale toiming"
algne_saldo = float(input("vali algne saldo: "))
while True:
    toiming = input("vali toimingu tüüp (väljavõte,deposiit): ")
    summa = float(input("vali summa: "))
    print(bank(algne_saldo,toiming,summa))
