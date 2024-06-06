from django.shortcuts import render


def homePage(request):
    if request.method == 'GET':
        print('get')
    else:
        print('NAWET KOLEGOM')

    context = {}
    return render(request, 'index.html', context)
