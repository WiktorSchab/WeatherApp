from django.shortcuts import render
from .forms import LocationForm


def homePage(request):
    if request.method == 'GET':
        form = LocationForm(request.GET)
        if form.is_valid():
            location = form.cleaned_data['location']

            context = {'location': location}
            return render(request, 'forecast.html', context)

    form = LocationForm()
    context = {'form': form}
    return render(request, 'index.html', context)
