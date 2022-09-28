from django.urls import path

from recipes.views import RecipeViews

recipeViews = RecipeViews()

urlpatterns = [
    path('', recipeViews.home, name='recipes-home'),
    path('recipes/<int:id>/', recipeViews.recipe, name='recipes-recipe')
]
