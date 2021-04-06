from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from recipes.models import Recipe


class RecipesListView(ListView):
    model = Recipe
    template_name = "index.html"
    paginate_by = 6
    context_object_name = "recipes"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "singlePage.html"
    context_object_name = "recipe"
    pk_url_kwarg = "recipe_id"

    def get_queryset(self):
        recipe = Recipe.objects.filter(id=self.kwargs['recipe_id'])
        return recipe
