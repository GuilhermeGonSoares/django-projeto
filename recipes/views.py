from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    
    return render(request, 'recipes/home.html', context={
        'name': 'Guilherme',
    })

def contato(request: HttpRequest) -> HttpResponse:

    return HttpResponse("<h2>Página de contatos</h2>")

def sobre(request: HttpRequest) -> HttpResponse:

    return HttpResponse("<h2>Página sobre</h2>")
