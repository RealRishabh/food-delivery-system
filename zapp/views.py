from django.db.models.fields import BooleanField
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User as userdj
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as login_kr

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('restaurants')

    if request.method == 'POST':
        user        = request.POST['userName']
        password    = request.POST['userPass']

        u = authenticate(username=user, password=password)
        if u is not None:
            login_kr(request, u)
            return redirect('restaurants')
        else:
            return render(request, 'login.html', {'msg':'Login Failed. Please try again.'})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username    = request.POST['userName']
        email       = request.POST['userEmail']
        password    = request.POST['userPass']
        cpass       = request.POST['userCpass']
        userType    = request.POST['btnradio']

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'msg':'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'msg':'Email already exists'})

        if password != cpass:
            return render(request, 'signup.html', {'msg':'Passwords do not match'})

        if userType == 'on':
            userType = 'Foodie'
        else:
            userType = "Resturant"

        User.objects.create(username=username, email=email, password=password, userType=userType)
        newUser = userdj.objects.create_user(username, email, password)
        newUser.save()

        messages.success(request, 'User created!')
        return redirect('login')

    return render(request, 'signup.html')

def restaurants(request):
    if request.user.is_authenticated:
        restaurant_obj = Restaurants.objects.all()
        return render(request, 'restaurants.html', {'restaurant_obj': restaurant_obj})
    else:
        messages.error(request, 'Please, login first then view restuarants page!')
        return redirect('login')


def restaurantPage(request, r_name):
    if request.user.is_authenticated:
        rest_dish = Dishes.objects.filter(dish_restaurant_name=r_name)
        rest_name = rest_dish[0].dish_restaurant_name
        return render(request, 'restaurantPage.html', {'rest_dish':rest_dish,'rest_name':rest_name})
    else:
        messages.error(request, 'Please, login first then view restuarants page!')
        return redirect('login')

def checkout(request, r_name):
    if request.method == "POST":
        user    = request.user.username
        bill    = request.POST['total']
        d_order = request.POST['items']

        Order_placed.objects.create(user_who_ordered=user, restaurant_of_order=r_name,dish_order=d_order,total_price=bill)

    if request.user.is_authenticated:
        d_price = Dishes.objects.filter(dish_restaurant_name=r_name)
        dish_p = []
        for i in d_price:
            dish_p.append(i.dish_price)
        # print(d_price[0].dish_price)
        return render(request, 'checkout.html',{'dish_p':dish_p})
    else:
        messages.error(request, 'Please, login first then view restuarants page!')
        return redirect('login')

def signout(request):
    logout(request)
    return redirect('login')