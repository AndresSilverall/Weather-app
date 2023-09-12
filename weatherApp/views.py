from django.shortcuts import render
from django.conf import settings
import requests
import datetime
import json


# Create your views here.
def weather_app(request):

    #API_KEY = settings.KEY
    #print(API_KEY)
    API_KEY = f'8d93ed2b737a6f91c8dfa80d73fa2c3f'

    date = datetime.datetime.now()

    get_city = request.POST.get("search")
    url = f'http://api.openweathermap.org/data/2.5/weather?q={get_city}&appid={API_KEY}'
    city_weather = requests.get(url.format(get_city))
    city_weather.json()
    weather = json.loads(city_weather.text)
    

    main_info_weather = {

        "City": weather["name"],
        "Country": weather["sys"]["country"],
        "Description": weather["weather"][0]["description"],
        "Temperature": str(weather["main"]["temp"])[0:2],
        "icon": weather["weather"][0]["icon"],
        "feels": str(weather["main"]['feels_like'])[0:2],
        "humidity": weather["main"]['humidity'],
        "speed": weather["wind"]['speed']

    }


    #testeando que funcione correctamente el llamado a la Weather API
    print("Ciudad: ", main_info_weather["City"])
    print("pais: ",main_info_weather["Country"] )
    print("descripcion: ", main_info_weather["Description"] )
    print("temperatura: ",main_info_weather["Temperature"] )
    print("image: ", main_info_weather["icon"] )
    print()

    context = {

        "data": main_info_weather,
        "date": date,

    }
    
    return render(request, "index.html", context)

