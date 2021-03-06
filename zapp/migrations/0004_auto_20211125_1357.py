# Generated by Django 3.2.9 on 2021-11-25 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0003_auto_20211125_1350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resturants',
            new_name='Restaurants',
        ),
        migrations.AlterModelOptions(
            name='restaurants',
            options={'verbose_name_plural': 'Restaurants'},
        ),
        migrations.RenameField(
            model_name='dishes',
            old_name='dish_resturant_name',
            new_name='dish_restaurant_name',
        ),
        migrations.RenameField(
            model_name='order_placed',
            old_name='resturant_of_order',
            new_name='restaurant_of_order',
        ),
        migrations.RenameField(
            model_name='restaurants',
            old_name='resturant_address',
            new_name='restaurant_address',
        ),
        migrations.RenameField(
            model_name='restaurants',
            old_name='resturant_name',
            new_name='restaurant_name',
        ),
    ]
