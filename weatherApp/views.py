from django.shortcuts import render
from django.http import JsonResponse
import requests
import json


# Create your views here.
def index(request):
    return render(request, "index.html")


def api_pokemon(request):
    url = "https://pokeapi.co/api/v2/pokemon-species/aegislash"
    response = requests.get(url)
    content = response.text
    x = json.loads(content)
    context = {"x":x}
    return render(request, "index.html",context )
