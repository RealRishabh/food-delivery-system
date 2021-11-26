from django.contrib import admin
from .models import User, Restaurants, Dishes, Order_placed

admin.site.site_header = 'Zomato'
admin.site.site_title = 'Zomato'
admin.site.index_title = 'Manage Dukaan'

class UserManage(admin.ModelAdmin):
    list_display = ('username','email','userType')
    search_fields = ('username','email','userType')

class RestaurantsManage(admin.ModelAdmin):
    list_display = ('restaurant_name','restaurant_address')
    search_fields = ('restaurant_name','restaurant_address')
    
class DishesManage(admin.ModelAdmin):
    list_display = ('dish_name','dish_price','dish_restaurant_name')
    search_fields = ('dish_name','dish_restaurant_name')

class OrderPlacedManage(admin.ModelAdmin):
    list_display = ('user_who_ordered','restaurant_of_order','dish_order','total_price','date')
    search_fields = ('user_who_ordered','dish_order')


admin.site.register(User,UserManage)
admin.site.register(Restaurants,RestaurantsManage)
admin.site.register(Dishes,DishesManage)
admin.site.register(Order_placed,OrderPlacedManage)