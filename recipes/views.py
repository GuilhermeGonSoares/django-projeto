from django.db.models import Q
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe


class RecipeViews:

    def home(self, request: HttpRequest) -> HttpResponse:
        recipes = Recipe.objects.filter(is_published=True).order_by('-id')
        
        return render(request, 'recipes/pages/home.html', context={
            'recipes': recipes
    })

    def category(self, request: HttpRequest, category_id: int) -> HttpResponse:
        #recipes = Recipe.objects.filter(category__id=category_id, is_published=True)
        
        #if not recipes:
        #    raise Http404('Not found!')
        def orderRecipe(recipe: Recipe) -> int:
            return recipe.id

        recipes = get_list_or_404(Recipe, category__id=category_id, is_published=True)
        recipes.sort(reverse=True, key=orderRecipe)
        

        return render(request, 'recipes/pages/category.html', context={
            'recipes': recipes,
            'category_name': f'{recipes[0].category.name} - Category | '
    })

    def recipe(self, request: HttpRequest, id: int) -> HttpResponse:
        #Tanto pela QuerySet quanto pela model + filtros
        #recipe = get_object_or_404(Recipe.objects.filter(pk=id))
        recipe = get_object_or_404(Recipe, pk=id, is_published=True)
        
        return render(request, 'recipes/pages/recipe-view.html', context={
            'recipe': recipe,
            'isDetailPage': True,
    })

    def search(self, request: HttpRequest) -> HttpResponse:
        query_param = request.GET.get('q', "").strip()

        recipes = Recipe.objects.filter(
            Q(
                Q(title__icontains=query_param) |
                Q(description__icontains=query_param)
            ),
            is_published=True
            ).order_by('-id')

        return render(request, 'recipes/pages/search.html', context={
            'filtered_recipes': recipes,
            'page_title': query_param.capitalize(),
            'search_form': query_param,
        })


