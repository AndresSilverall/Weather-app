from django.shortcuts import render
from django.conf import settings
import requests
import datetime
import json


# Create your views here.
def weather_app(request):

    #API_KEY = settings.KEY
    #print(API_KEY)
    API_KEY = f'66e0ca6918000599b7f60957e1b55812'

    date = datetime.datetime.now()

    get_city = request.POST.get("search")
    url = f'http://api.openweathermap.org/data/2.5/weather?q={get_city}&appid={API_KEY}'
    city_weather = requests.get(url.format(get_city))
    city_weather.json()
    clima = json.loads(city_weather.text)
    print(clima)
    
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

    }
    
    return render(request, "index.html", context)

