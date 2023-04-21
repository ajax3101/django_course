import os
import requests
from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv, find_dotenv





load_dotenv(find_dotenv())
wak = os.environ.get("YOUR_API_KEY")



def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, wak)
        response = requests.get(url)
        data = response.json()
        if data['cod'] == '404':
            return HttpResponse(f'<script>alert("City {city} does not exist!");</script>')
        country = data['sys']['country']
        coords = data['coord']
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        return render(request, 'weather/weather.html', {'city': city, 'country': country, 'coords': coords, 'weather': weather, 'temp': temp})
    else:
        return render(request, 'weather/index.html')
