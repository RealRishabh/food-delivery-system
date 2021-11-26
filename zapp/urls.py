from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('restaurants', views.restaurants, name='restaurants'),
    path('checkout<str:r_name>', views.checkout, name='checkout'),
    path('signout', views.signout, name='signout'),
    path('restaurants_page<str:r_name>', views.restaurantPage, name='restaurantPage'),
]