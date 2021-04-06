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


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    search_fields = ('user', 'author',)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user', 'recipe',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientsForRecipe, IngredientsForRecipeAdmin)
admin.site.register(Follow)
admin.site.register(Favorite, FavoriteAdmin)
