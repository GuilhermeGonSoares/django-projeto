from django.urls import path

from recipes.views import RecipeViews

recipeViews = RecipeViews()

urlpatterns = [
    path('', recipeViews.home, name='recipes-home'),
    path('recipes/search', recipeViews.search, name='recipes-search'),
    path('recipes/category/<int:category_id>/', recipeViews.category, name='recipes-category'),
    path('recipes/<int:id>/', recipeViews.recipe, name='recipes-recipe'),
]
