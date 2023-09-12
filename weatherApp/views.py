from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests
import datetime
import json


# Create your views here.
import requests
import datetime
import json
from django.shortcuts import render

def weather_app(request):
    API_KEY = '8d93ed2b737a6f91c8dfa80d73fa2c3f'
    date = datetime.datetime.now()
    main_info_weather = {}  # Initialize the dictionary

    if request.method == "POST":
        get_city = request.POST.get("search")
        url = f'http://api.openweathermap.org/data/2.5/weather?q={get_city}&appid={API_KEY}'
        city_weather = requests.get(url)
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

    context = {
        "data": main_info_weather,
        "date": date,
    }

    return render(request, "index.html", context)

