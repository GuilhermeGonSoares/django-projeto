from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe


class RecipeViews:

    def home(self, request: HttpRequest) -> HttpResponse:
        
        return render(request, 'recipes/pages/home.html', context={
            'recipes': [make_recipe() for _ in range(9)]
    })

    def recipe(self, request: HttpRequest, id: int) -> HttpResponse:
        return render(request, 'recipes/pages/recipe-view.html', context={
            'recipe': make_recipe(),
            'isDetailPage': True,
    })


