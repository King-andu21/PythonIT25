import os
import datetime
x = datetime.datetime.now()
kuupaev = x.strftime("%x")
kuupaev = kuupaev.replace("/","-")
tookataloog_name = f"{os.getlogin()}_tookataloog_{kuupaev}"
print(kuupaev)

try:
    print(f"genereerime kataloogi: {tookataloog_name}")
    os.mkdir(f"PythonIT25/{tookataloog_name}")
except FileExistsError:
    print(f"{tookataloog_name} eksisteerib juba")
# Op name
print(f"os nimi: {os.name}")
# Logged in account name
print(f"Tere {os.getlogin()}")

# praegune kaust
print(f"Asukoht: {os.getcwd()}")
# kausta sisu
print(f"Esemed: {os.listdir()}")
creation_amount = int(input("mitu kataloogi soovid luua?: "))
print(creation_amount)
for i in range (creation_amount):
    try:
       os.mkdir(f"PythonIT25/{tookataloog_name}/uus_kaust_nr{i+1}")
    except FileExistsError:
       print(f"Kataloog uus_kaust_nr{i+1} juba eksisteerib.")
print(f"kausta sisu: {os.listdir(f"PythonIT25/{tookataloog_name}")}")
selected_for_del = int(input("millist kataloogi soovid kustutada? (number): "))
try:
    os.rmdir(f"PythonIT25/{tookataloog_name}/uus_kaust_nr{selected_for_del}")
except FileNotFoundError:
    print(f"uus_kaust_nr{selected_for_del} pole olemas.")
else: 
    print(f"kaust uus_kaust_nr{selected_for_del} leitud ja kustutatud")