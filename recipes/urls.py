from django.urls import path

from recipes.views import RecipesListView, RecipeDetailView

urlpatterns = [
    path("", RecipesListView.as_view(), name="index"),
    path("<int:recipe_id>/", RecipeDetailView.as_view(), name="recipe"),
]

