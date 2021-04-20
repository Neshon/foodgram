from django import forms
from django.shortcuts import get_object_or_404

from .models import Recipe, IngredientsForRecipe, Ingredient


class RecipeForm(forms.ModelForm):
    # ingredients = forms.CharField(
    #     required=False,
    #     label="Ингредиенты",
    #     widget=forms.TextInput(attrs={"id", "nameIngredient"}),
    # )

    class Meta:
        model = Recipe
        fields = ("title", "tag", "cooking_time", "description", "image")
        labels = {
            "title": "Название рецепта",
            "description": "Описание",
        }
        widgets = {
            "cooking_time": forms.TextInput(),
            "tag": forms.CheckboxSelectMultiple(),
        }

    def clean_ingredients(self):
        ingredients = list(
            zip(
                self.data.getlist('nameIngredient'),
                self.data.getlist('valueIngredient'),
            ),
        )
        if not ingredients:
            raise forms.ValidationError('Отсутствуют ингредиенты')

        ingredients_clean = []
        for name, amount in ingredients:
            if int(amount) < 1:
                raise forms.ValidationError(
                    f'Исправьте количество ингредиента "{name}"')
            else:
                ingredients_clean.append({
                    'title': name,
                    'amount': amount,
                })
        return ingredients_clean

    def save(self, commit=True):
        recipe = super().save(commit=False)
        recipe.save()

        ingredients_in_recipes = []
        for title, amount in self.ingredients:
            ingredient = get_object_or_404(Ingredient, title=title)
            ingredients_in_recipes.append(
                IngredientsForRecipe(
                    recipe=recipe, ingredient=ingredient, amount=amount))

        IngredientsForRecipe.objects.filter(recipe=recipe).delete()
        IngredientsForRecipe.objects.bulk_create(ingredients_in_recipes)
        self.save_m2m()
        return recipe
