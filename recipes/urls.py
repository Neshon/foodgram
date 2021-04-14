from django.urls import path

from recipes.views import RecipesListView, RecipeDetailView, FollowRecipesListView

urlpatterns = [
    path("", RecipesListView.as_view(), name="index"),
    path("follow/", FollowRecipesListView.as_view(), name="follow"),
    path("<int:recipe_id>/", RecipeDetailView.as_view(), name="recipe"),
]
