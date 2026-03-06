import requests

# API võtme ja linna nime määramine
city = input("Linn: ")
city = city.strip().capitalize()
print("sinu otsing",city)
api_key = "95b59704ef238b5e7a6d27d49270166d"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# API päringu tegemine
response = requests.get(url)

# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    feels_like = data["main"]["feels_like"]
    print(f"Ilma kirjeldus: {weather}")
    print(f"Temperatuur: {temperature} °C")
    print(f"Tundub nagu: {feels_like} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)
print(response.json())