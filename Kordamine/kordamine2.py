#1. Products
# ā€¢ Kuva toodete nimed ja hinnad (title, price) 
# ā€¢ Leia kĆµige kallim toode 
# ā€¢ Filtreeri tooted, mille laoseis on  < 20 
# ā€¢ Arvuta keskmine hind 

import requests

url = f"https://metshein.com/kordamine/json/tooted.json"

response = requests.get(url)

tooted_amount = 0
tooted_20amount = 0
highest_price = 0
total_price = 0
filter_mode = input("vali filtri moodus(1=>;2=<): ")
filter_mode = int(filter_mode)
if response.status_code == 200:
    data = response.json()
    id = data['tooted'][0]['id']
    
    for i in data['tooted']:
        amount = data['tooted'][tooted_amount]['laoseis']
        if filter_mode == 1 and amount >20 or filter_mode == 2 and amount <20:
            name = data['tooted'][tooted_amount]['nimi']
            price = data['tooted'][tooted_amount]['hind']
            total_price = total_price+price
            if price > highest_price:
                highest_price = data['tooted'][tooted_amount]['hind']
                hp_name = data['tooted'][tooted_amount]['nimi']
                print(f"Toote nimi: {name}")
                print(f"Toote hind: {price}")
                print(f"-----------")
            tooted_20amount +=1
        tooted_amount +=1
    avarege_price = total_price/tooted_20amount
        
else:
    print("Viga andmete allalaadimisel:", response.status_code)
#print(response.json())
print(f"filtreeritud Kõige kallim toode: {hp_name}, {highest_price}")
print(f"eri toodete kogus kogu laos: {tooted_amount}")
print(f"filtreeritud toodete kogus: {tooted_20amount}")
print(f"filtreeritud keskmine toote hind: {avarege_price}")