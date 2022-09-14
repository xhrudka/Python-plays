import requests

api_key = "2d3e0b77c4313b4ec38927d782e6f8e3"
city = "Prague"
url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()
print(json)
description= json.get("weather")[0].get("description")
print("Today's the forecast is", description)
temp_min= json.get('main').get("temp_min")
print("The minimum temperature is", temp_min)