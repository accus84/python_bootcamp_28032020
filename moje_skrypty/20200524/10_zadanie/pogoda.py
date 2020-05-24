"""
Korzystajac z API pogodowego (MetaWeather)
https://www.metaweather.com/api/
#pobierz dane
$ python pogoda.py warsaw
Pogoda w warsaw:
Temperatura: 15 stopni C.
Wilgotność:  67 %
Ciśnienie powietrza: 1111 hPa
"""

import sys
import requests

if len(sys.argv) > 1:                   #jeśli po uruchomieniu przez terminal będzie więcej niż 1 argument (czyli coś oprócz nazwy pliku)
    location_name = sys.argv[1]         #to tym argumentem dodatkowym będzie location_name
else:
    location_name = "Warsaw"            #a jak nie to domyślnie będzie Warsaw

def get_location_id(location_name):
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={location_name}")
    woeid = resp.json()[0]["woeid"]
    return woeid

woeid = get_location_id(location_name)

def get_location_weather(location_id):
    resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    temp = resp.json()["consolidated_weather"][0]["the_temp"]
    humidity = resp.json()["consolidated_weather"][0]["humidity"]
    air_pressure = resp.json()["consolidated_weather"][0]["air_pressure"]

    weather = print(f"""
    Pogoda w {location_name}:
    Temperatura: {temp}
    Wilgotność: {humidity}
    Ciśnienie powietrza: {air_pressure}
    """)

    return weather

print(get_location_weather(woeid))