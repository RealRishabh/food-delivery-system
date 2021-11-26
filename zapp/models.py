from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    def __str__(self):
        return self.username

    username    = models.CharField(max_length=10)
    email       = models.EmailField(max_length=254, null=True)
    password    = models.CharField(max_length=100)
    userType    = models.CharField(max_length=10)
        
    class Meta:
        verbose_name_plural = "Users"

class Restaurants(models.Model):
    def __str__(self) -> str:
        return self.restaurant_name

    restaurant_name       = models.CharField(max_length=100, null=True)
    restaurant_address    = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Restaurants"

class Dishes(models.Model):
    def __str__(self) -> str:
        return self.dish_name

    dish_name            = models.CharField(max_length=100, null=True)
    dish_price           = models.IntegerField(null=True)
    dish_restaurant_name = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Dishes"

class Order_placed(models.Model):
    def __str__(self) -> str:
        return self.user_who_ordered

    user_who_ordered    = models.CharField(max_length=100, null=True)
    restaurant_of_order = models.CharField(max_length=100, null=True)
    dish_order          = models.CharField(max_length=100, null=True)
    total_price         = models.IntegerField(null=True)
    date                = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "OrderPlaced"