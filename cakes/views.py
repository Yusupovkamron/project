from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from .models import Sweets, Discounts, Masters, Clients, Locations
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response



class SweetsListView(APIView):
    def get(self, request):
        sweets = Sweets.objects.all()
        discounts = Discounts.objects.all()
        masters = Masters.objects.all()
        clients = Clients.objects.all()
        locations = Locations.objects.all()
        context = {
            "sweets": sweets,
            "discounts": discounts,
            "masters": masters,
            "clients": clients,
            "locations": locations,
        }
        return render(request, "main/index.html", context)


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'main/login.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password_1']
        password2 = request.POST['password_2']
        if password1 != password2:
            return redirect('register')
        else:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password1)
            user.save()
            return redirect('login')

class DiscountsView(View):
    def get(self, request, id):
        product = Discounts.objects.get(id=id)
        Discounts.objects.create(product=product)
        price = 0
        shipping_price = 0
        for cart_product in Discounts.objects.all():
            price += cart_product.product.price
            shipping_price = cart_product.shipping_price
        cart = Discounts.objects.all()
        context = {
            'cart': cart,
            'price_ship': price + shipping_price,
            'price': price,
            'shipping_price': price,
        }
        return render(request, 'about.html', context)