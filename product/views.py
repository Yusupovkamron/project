from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from .models import Products, Services
from cakes.models import Sweets, Discounts, Masters, Clients, Locations
from rest_framework.views import APIView

class ProductsApiView(APIView):
    def get(self, request):

        services = Services.objects.all()
        products = Products.objects.all()
        context = {
            "services": services,
            "products": products,

        }
        return render(request, "main/menu.html", context)


class ServicesApiView(APIView):
    def get(self, request):
        return render(request, "main/service.html")