from django.shortcuts import render
from .forms import LocationForm
from .utilities import get_daily_temps
import requests


def homePage(request):
    if request.method == 'GET':
        form = LocationForm(request.GET)
        if form.is_valid():
            location = form.cleaned_data['location']

            api_link = r'https://api.openweathermap.org/data/2.5/forecast'
            api_key = open('./api_key', 'r').read().strip()

            # Handling countries will be added in future
            city = location

            # Construct the API request URL
            url = f"{api_link}?q={city}&cnt=40&appid={api_key}"

            # Getting response from api
            response = requests.get(url).json()

            city_info = response['city']
            weather_info = response['list']
            weather_daily_info = get_daily_temps(weather_info)
            print(weather_daily_info)
            context = {'city_info': city_info,
                       'weather_info': weather_info,
                       'weather_daily_info': weather_daily_info,}

            return render(request, 'forecast.html', context)

    form = LocationForm()
    context = {'form': form}
    return render(request, 'index.html', context)
