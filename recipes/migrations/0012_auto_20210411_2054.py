# Generated by Django 3.1.7 on 2021-04-11 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20210411_2049'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='favorite',
            name='user_not_recipe',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='user_not_author',
        ),
        migrations.RemoveConstraint(
            model_name='purchase',
            name='not_unique_purchase',
        ),
    ]
