import json
import requests
import time


api_key = "9e862f3308bb2afb0be69a33118db597"
lat = 47.238435
lon = 9.598354

url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}"
url = url.format(lat = lat, lon = lon, key = api_key)

r = requests.get(url)
request = r.json()

for element in request:
    print('{} -> {}'.format(element, request[element]))

temp = round(request["main"]["temp"])

print('\n\nThe temperature in {} is {}°'.format(request["name"], temp))

# Just in case, so in no case the max request / second is exceeded
time.sleep(1)