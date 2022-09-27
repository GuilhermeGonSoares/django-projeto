from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Guilherme',
    })

