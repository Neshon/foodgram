from django.contrib import admin
from recipes.models import *


class RecipeIngredientInline(admin.TabularInline):
    model = IngredientsForRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline,)
    list_display = ("title", "author", "pub_date", "cooking_time", "tag")
    search_fields = ("title", )
    list_filter = ("pub_date", )


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("title", "unit")
    search_fields = ("title", )


class IngredientsForRecipeAdmin(admin.ModelAdmin):
    list_display = ("recipe", "ingredient", "amount")


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientsForRecipe, IngredientsForRecipeAdmin)

