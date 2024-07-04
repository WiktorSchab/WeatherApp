from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LocationForm
from .utilities import get_daily_temps, get_hour_weather, get_iso_country_tag, get_english_country_name

import requests
import json


def homePage(request):
    if request.method == 'GET':
        form = LocationForm(request.GET)
        if form.is_valid():
            location = form.cleaned_data['location']

            api_link = r'https://api.openweathermap.org/data/2.5/forecast'
            api_key = open('./api_key', 'r').read().strip()

            # Getting city
            location = location.split(',')
            city = location[0]

            # Checking if user gave country
            if len(location) > 1:
                country = location[1].strip()

                # Getting English country name
                country_eng = get_english_country_name(country)

                # Getting ISO country tag
                country_iso = get_iso_country_tag(country_eng)

                if country_iso:
                    city = ', '.join([city, country_iso])
                else:
                    messages.error(request, "Country Error | Country wasn't found. Please note that the country name must be in English.")
                    return redirect('homePage')

            # Construct the API request URL
            url = f"{api_link}?q={city}&cnt=40&appid={api_key}"

            # Getting response from api
            response = requests.get(url).json()

            if response['cod'] == '200':
                city_info = response['city']
                weather_info = get_hour_weather(response['list'])
                weather_daily_info = get_daily_temps(response['list'])

                # Converting values of the dict into a JSON file to pass it to the javascript
                weather_data_for_chart = {}
                for date, info in weather_info.items():
                    weather_data_for_chart[date] = json.dumps(info)

                context = {'city_info': city_info,
                           'weather_info': weather_data_for_chart,
                           'weather_daily_info': weather_daily_info,}
                return render(request, 'forecast.html', context)
            else:
                messages.error(request, f'Error {response["cod"]} | {response["message"]}')
                return redirect('homePage')

    form = LocationForm()
    context = {'form': form}
    return render(request, 'index.html', context)
