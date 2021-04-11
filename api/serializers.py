from rest_framework import serializers

from recipes.models import Ingredient, Follow, Favorite, Purchase


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("user", "author")
        model = Follow


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("recipe", )
        model = Favorite


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("recipe", )
        model = Purchase


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("title", "unit")
        model = Ingredient
