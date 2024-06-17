from django.shortcuts import render
from .forms import LocationForm
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

            context = {'location': response}
            return render(request, 'forecast.html', context)

    form = LocationForm()
    context = {'form': form}
    return render(request, 'index.html', context)
