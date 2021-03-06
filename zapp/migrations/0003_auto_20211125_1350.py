# Generated by Django 3.2.9 on 2021-11-25 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0002_auto_20211123_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_placed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_who_ordered', models.CharField(max_length=100, null=True)),
                ('resturant_of_order', models.CharField(max_length=100, null=True)),
                ('dish_order', models.CharField(max_length=100, null=True)),
                ('total_price', models.IntegerField(null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'OrderPlaced',
            },
        ),
        migrations.DeleteModel(
            name='OrderPlaced',
        ),
        migrations.RemoveField(
            model_name='dishes',
            name='dishName',
        ),
        migrations.RemoveField(
            model_name='dishes',
            name='dishPrice',
        ),
        migrations.RemoveField(
            model_name='dishes',
            name='dishResturantName',
        ),
        migrations.RemoveField(
            model_name='resturants',
            name='resturantAddress',
        ),
        migrations.RemoveField(
            model_name='resturants',
            name='resturantName',
        ),
        migrations.AddField(
            model_name='dishes',
            name='dish_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dishes',
            name='dish_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='dishes',
            name='dish_resturant_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resturants',
            name='resturant_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resturants',
            name='resturant_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
