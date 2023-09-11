from django.shortcuts import render
from django.http import JsonResponse
from .forms import SearchCity
import requests
import datetime
import json


# Create your views here.
def index(request):
    return render(request, "index.html")


def api_pokemon(request):

    form = SearchCity()
    date = datetime.datetime.now()
    
    API_KEY = "8d93ed2b737a6f91c8dfa80d73fa2c3f"
    city = f"Medellín, CO"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    city_weather = requests.get(url.format(city))
    city_weather.json()
    clima = json.loads(city_weather.text)
    
    info = {

        "City": clima["name"],
        "Country": clima["sys"]["country"],
        "Description": clima["weather"][0]["description"],
        "Temperature": round(clima["main"]["temp"], ndigits=None),
        "icon": clima["weather"][0]["icon"]
    }


    #testeando que funcione correctamente el llamado a la Weather API
    print("Ciudad: ", info["City"])
    print("pais: ",info["Country"] )
    print("descripcion: ", info["Description"] )
    print("temperatura: ",info["Temperature"] )
    print("image: ", info["icon"] )
    print()

    context = {

        "data": info,
        "date": date,
        "form": form

        }
    return render(request, "index.html", context)
