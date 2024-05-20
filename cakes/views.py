from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from .models import Sweets, Discounts, Masters, Clients, Locations
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .serializers import MastersSerializer, ClientsSerializer



class SweetsListView(APIView):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            sweets = Sweets.objects.all()
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
        else:
            sweets = Sweets.objects.filter(title__icontains=search)
            if sweets:
                context = {
                   "sweets": sweets
                }

                return render(request, 'main/index.html', context)
            else:
                context = {
                    "sweets": sweets,

                }
                return render(request, 'main/not.html', context)

        # sweets = Sweets.objects.all()
        # discounts = Discounts.objects.all()
        # masters = Masters.objects.all()
        # clients = Clients.objects.all()
        # locations = Locations.objects.all()
        # context = {
        #     "sweets": sweets,
        #     "discounts": discounts,
        #     "masters": masters,
        #     "clients": clients,
        #     "locations": locations,
        # }
        # return render(request, "main/index.html", context)



class UsersLoginView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            user = User.objects.all()
            context = {
                "user": user,
            }
            return render(request, "main/login.html", context)


        else:
            user = User.objects.filter(first_name__icontains=search)
            if user:
                context = {
                    "user": user
                }

                return render(request, 'main/login.html', context)
            else:
                context = {
                    "user": user
                }
            return render(request, 'main/not.html', context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {'username': username,
                'password': password
                }
        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('landing')
        else:
            return render(request, 'main/404.html')

class MastersSetView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            masters = Masters.objects.all()
            context = {
                "masters": masters,
            }
            return render(request, "main/team.html", context)

        else:
            masters = Masters.objects.filter(first_name__icontains=search)
            if masters:
                context = {
                   "masters": masters
                }

                return render(request, 'main/team.html', context)
            else:
                context = {
                    "masters": masters
                }
                return render(request, 'main/not.html', context)



class SweetView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            sweets = Sweets.objects.all()
            context = {
                "sweets": sweets,
            }
            return render(request, "main/manu.html", context)

        else:
            sweets = Sweets.objects.filter(name__icontains=search)
            if sweets:
                context = {
                    "sweets": sweets
                }

                return render(request, 'main/manu.html', context)
            else:
                context = {
                    "sweets": sweets
                }
                return render(request, 'main/index.html', context)


class DiscountsView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            discounts = Discounts.objects.all()
            context = {
                "discounts": discounts
            }
            return render(request, "main/about.html", context)
        else:
            discounts = Discounts.objects.filter(title__icontains=search)
            if discounts:
                context = {
                    "discounts": discounts
                }

                return render(request, 'main/about.html', context)
            else:
                context = {
                    "discounts": discounts
                }
                return render(request, 'main/not.html', context)


class LocationsView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            locations = Locations.objects.all()
            context = {
                "locations": locations,
            }
            return render(request, "main/contact.html", context)
        else:
            locations = Locations.objects.filter(first_name__icontains=search)
            if locations:
                context = {
                   "locations": locations
                }

                return render(request, 'main/contact.html', context)
            else:
                context = {
                    "locations": locations
                }
                return render(request, 'main/not.html', context)







class UserRegisterView(View):
    def get(self, request):
        def get(self, request):
            search = request.GET.get("search")
            if not search:
                register = User.objects.all()
                context = {
                    "register": register,
                }
                return render(request, "main/register.html", context)

            else:
                register = User.objects.filter(first_name__icontains=search)
                if register:
                    context = {
                        "register": register
                    }

                    return render(request, 'main/register.html', context)
                else:
                    context = {
                        "register": register
                    }
                    return render(request, 'main/not.html', context)


    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_2"]

        user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password_1)
        user.save()
        return redirect("discounts")

class ClientsViewApiSet(APIView):
    filter_backends = (filters.SearchFilter,)
    search_fields = ['^title']
    # pagination_class = LimitOffsetPagination
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            clients = Clients.objects.all()
            context = {
                "clients": clients,
            }
            return render(request, "main/testimonial.html", context)
        else:
            clients = Clients.objects.filter(first_name__icontains=search)
            if clients:
                context = {
                    "clients": clients
                }

                return render(request, 'main/testimonial.html', context)
            else:
                context = {
                    "clients": clients
                }
                return render(request, 'main/not.html', context)
class RegisterApiView(APIView):
    def get(self, request):
        return render(request, "main/register.html")





"""
Tasklar: Web Application uchun: 1. Login 2. Register 3. Authentication (LoginMixView) 
4. Har bir model uchun View yozishda get, post, update, delete qismlari ishlashi kerak
 va ular button orqali amalga oshirilsin 5. Har bir model search qilish imkoniyatiga ega bo'lsin. 
 6. Admin panelda search, ordering, import va export qismlari ham qo'shilsin. 
 7. Biror modelni qidirish uchun id orqali emas slug orqali qidirish imkoniyatiga ega bo'lsin. 
 API Application uchun: 1. Authentication and Permission qismlari bo'lsin 
 2. Har bir model api orqali search qila olsin(bir yoki bir nechta parametrlari orqali) 
 3. Har bir model uchun qiymatga ega 3 tadan action yaratilsin. 4. Viewlarni ModelViewSet lar orqali yating. 
 5. Swagger yoki Redoc documentionga ega bo'lsin. 6. Kamida bitta model uchun rewies parametrga ega bo'lsin.
  Va bunda manashu objectga har safar click bo'lganda ko'rishlar soni yoki eshitishlar soni 
  1 taga oshib boradigan action qo'shilsin. 7. Modellar ga meta class qo'shing.
"""