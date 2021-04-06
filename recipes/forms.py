from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(
        required=False,
        label="Ингредиенты",
        widget=forms.TextInput(attrs={"id", "nameIngredient"})
    )

    class Meta:
        model = Recipe
        fields = ("title", "tag", "ingredients", "cooking_time", "description", "image")
        labels = {
            "title": "Название рецепта",
            "description": "Описание",
        }
        widgets = {
            "cooking_time": forms.TextInput(),
        }

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.save()
    #     ingredients = self.cleaned_data["ingredients"]
    #     self.cleaned_data["ingredients"] = []
    #     self.save_m2m()
    #
    #     return instance
