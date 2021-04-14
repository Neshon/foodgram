from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from recipes.forms import RecipeForm
from recipes.models import Recipe, User


class RecipesListView(ListView):
    model = Recipe
    template_name = "index.html"
    paginate_by = 6
    context_object_name = "recipes"


class FollowRecipesListView(ListView):
    model = User
    template_name = 'myFollow.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            following__user=self.request.user).order_by('-id')


class FavoriteRecipesListView(ListView):
    model = Recipe
    template_name = 'favorite.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(favorites__user=self.request.user)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "singlePage.html"
    context_object_name = "recipe"
    pk_url_kwarg = "recipe_id"

    def get_queryset(self):
        recipe = Recipe.objects.filter(id=self.kwargs['recipe_id'])
        return recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "new_recipe.html"

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = self.request.user
        recipe.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("index")
