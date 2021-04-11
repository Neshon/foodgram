from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    # ingredients = forms.CharField(
    #     required=False,
    #     label="Ингредиенты",
    #     widget=forms.TextInput(attrs={"id", "nameIngredient"}),
    # )

    class Meta:
        model = Recipe
        fields = ("title", "tag", "ingredients", "cooking_time", "description", "image")
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
        for name, quantity in ingredients:
            if int(quantity) < 1:
                raise forms.ValidationError(
                    f'Исправьте количество ингредиента "{name}"')
            else:
                ingredients_clean.append({
                    'title': name,
                    'quantity': quantity,
                })
        return ingredients_clean

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()
        ingredients = self.cleaned_data["ingredients"]
        self.cleaned_data["ingredients"] = []
        self.save_m2m()

        return instance
