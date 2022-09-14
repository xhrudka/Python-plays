import requests

def get_weather_desc_and_temp():
    api_key = "2d3e0b77c4313b4ec38927d782e6f8e3"
    city = "Prague"
    url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()
    print(json)
    description= json.get("weather")[0].get("description")
    temp_min= json.get('main').get("temp_min")

    return{"description": description, "temp_min": temp_min,}
# Print the results

def main():

    weather_dict=get_weather_desc_and_temp()
    print("Today's the forecast is", weather_dict.get("description"))
    print("The minimum temperature is", weather_dict.get("temp_min"))

main()