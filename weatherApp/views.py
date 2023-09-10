from django.shortcuts import render
from django.http import JsonResponse
import requests
import json


# Create your views here.
def index(request):
    return render(request, "index.html")


def api_pokemon(request):
    API_KEY = "8d93ed2b737a6f91c8dfa80d73fa2c3f"
    city = f"Barranquilla,CO"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    city_weather = requests.get(url.format(city))
    city_weather.json()
    clima = json.loads(city_weather.text)
    
    data = {
        "city": clima["name"],
        "country": clima["sys"]["country"],
        "desc": clima["weather"][0]["description"],
        "temp": clima["main"]["temp"],
        "icon": clima["weather"][0]["icon"]
    }

    print("Ciudad: ", data["city"])
    print("pais: ",data["country"] )
    print("descripcion: ", data["desc"] )
    print("temperatura: ",data["temp"] )
    print("imagen: ", data["icon"] )
    print()

    return render(request, "index.html" )
