from urllib import response
import requests
response=requests.get("http://api.open-notify.org/astros.json")
json=response.json()

for person in json["people"]:
    print(person["name"])
    