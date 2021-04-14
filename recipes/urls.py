from django.urls import path

from recipes.views import RecipesListView, RecipeDetailView, FollowRecipesListView, FavoriteRecipesListView

urlpatterns = [
    path("", RecipesListView.as_view(), name="index"),
    path("follow/", FollowRecipesListView.as_view(), name="follow"),
    path("favorites/", FavoriteRecipesListView.as_view(), name="favorites"),
    path("<int:recipe_id>/", RecipeDetailView.as_view(), name="recipe"),
]
