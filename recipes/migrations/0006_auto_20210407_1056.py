# Generated by Django 3.1.7 on 2021-04-07 07:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_remove_recipe_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientsforrecipe',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Количество'),
        ),
    ]
