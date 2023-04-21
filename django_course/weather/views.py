import os
import requests
from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv, find_dotenv





load_dotenv(find_dotenv())
wak = os.environ.get("YOUR_API_KEY")

def index(request):
    return render(request, 'weather/index.html')

def weather(request):
    city = request.GET.get('city')
    print(city)
    if not city:
        return HttpResponse('Please provide a city name.')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={wak}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == '404':
        return HttpResponse(f'<script>alert("City {city} does not exist!");</script>')
    country = data['sys']['country']
    coords = data['coord']
    weather = data['weather'][0]['main']
    temp = data['main']['temp']
    return render(request, 'weather.html', {'city': city, 'country': country, 'coords': coords, 'weather': weather, 'temp': temp})
