# Generated by Django 3.1.7 on 2021-04-11 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20210411_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='author',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='user',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
