from django.shortcuts import render


def index(request):
    data = {
        'title': 'Home page',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
