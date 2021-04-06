from django.contrib.auth import get_user_model
from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator
from slugify import slugify

User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(max_length=70, verbose_name="Название")
    unit = models.CharField(max_length=20, verbose_name="Единица измерения")

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Recipe(models.Model):
    TYPES_OF_MEALS = (
        ("BREAKFAST", "breakfast"),
        ("LUNCH", "lunch"),
        ("DINNER", "dinner")
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ["-pub_date"]

    title = models.CharField(max_length=100, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание")
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Время публикации")
    tag = MultiSelectField(choices=TYPES_OF_MEALS,
                           default="BREAKFAST",
                           verbose_name="Теги")
    cooking_time = models.PositiveIntegerField(
        verbose_name="Время приготовления, мин.",
        help_text="в минутах",
        validators=[MinValueValidator(1)]
    )
    # slug = models.SlugField(max_length=120, blank=True, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="recipes",
                               verbose_name="Автор")
    ingredients = models.ManyToManyField(Ingredient,
                                         blank=False,
                                         through="IngredientsForRecipe",
                                         related_name="recipes",
                                         verbose_name="Ингредиенты")
    image = models.ImageField(upload_to="images/", verbose_name="Фото")

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)


class IngredientsForRecipe(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name="ingredients_recipe",
                               verbose_name="Рецепт")
    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.CASCADE,
                                   related_name="ingredients_recipe",
                                   verbose_name="Ингредиент")
    amount = models.PositiveIntegerField(validators=[MinValueValidator(0)],
                                         verbose_name="Количество")

    class Meta:
        verbose_name_plural = "Ингредиенты для рецепта"
        verbose_name = "Ингредиент для рецепта"


class Follow(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="follower",
                             verbose_name="Пользователь"
                             )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="following",
                               verbose_name="Автор"
                               )

    class Meta:
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "author"],
                name="unique_user_author"
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F("author")),
                name="user_not_author"
            )
        ]


class Favorite(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="favorites",
                             verbose_name="Пользователь")
    recipe = models.ForeignKey(Recipe, models.CASCADE,
                               related_name="favorites",
                               verbose_name="Рецепт")

    class Meta:
        verbose_name_plural = "Избранное"
