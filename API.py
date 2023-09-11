import requests
import json
import pprint

#GET method
def get_data_from_api():

    URL = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(URL)

    if response.status_code == 200:
        response.json()
        pprint.pprint(response.content)

    else:
        print("error")


#POST
def post_data():
    new_data = {
        "name": "andres",
        "age": 23,
        "position": "DevOps"
    }

    url = "https://jsonplaceholder.typicode.com/posts/1"
    headers = {'Content-Type':'application/json; charset=UTF-8'}
    response = requests.post(url, data=json.dumps(new_data), headers=headers)
    response.json()
    data = json.loads(response.text)
    print(data)
    


#PUT
def put_data():
    new_user = {
        "userId": 342,
        "id": 1048224831,
        "title": "hacking DRM",
        "body": "once upon in a time that I started with django"
    }
    url = "https://jsonplaceholder.typicode.com/posts/1"
    headers = {'Content-Type':'application/json; charset=UTF-8'}
    response = requests.put(url, data=json.dumps(new_user), headers=headers)
    print(response.text)




#DELETE
def delete_item_from_server():
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.delete(url, headers=headers)
    print(response.text)




def api_weather() -> str:
    API_KEY = "8d93ed2b737a6f91c8dfa80d73fa2c3f"
    city = f"Bogota, CO"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    city_weather = requests.get(url.format(city))
    city_weather.json()
    clima = json.loads(city_weather.text)
    
    data = {
        "city": clima["name"],
        "country": clima["sys"]["country"],
        "desc": clima["weather"][0]["description"],
        "temp": clima["main"]["temp"],
        "icon": clima["weather"][0]["icon"],
        "feels": clima["main"]["feels_like"]
    }

    print("Ciudad: ", data["city"])
    print("pais: ",data["country"] )
    print("descripcion: ", data["desc"] )
    print("temperatura: ",data["temp"] )
    print("imagen: ", data["icon"] )
    print("se siente: ", data["feels"] )
    print()


api_weather()

