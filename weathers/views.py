import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
import environ
from pathlib import Path
import os


def index(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    env = environ.Env()
    environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))
    appid = env('APP_ID')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.order_by('-id')

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
