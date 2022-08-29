#openweathermap.org
import requests
api_key="67da29cb91129f1a68c1c06c1be92daa"

#current weather data
city = "Orlando"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()
#print(json)
#The put the json into the json formatter to be able to read it
description = json.get("weather")[0].get("description")
print("Today's forecast is", description)
temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min)
temp_max = json.get("main").get("temp_max")
print("The maximum temperature is", temp_max)
