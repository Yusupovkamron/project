from django.contrib import admin
from .models import Sweets, Discounts, Masters, Clients, Locations
from import_export.admin import ImportExportModelAdmin



@admin.register(Sweets)
class SweetsAdmin(ImportExportModelAdmin):
    list_display = ('id', "name", "title", "image", 'x_link', "quality", "price", "price_type", "created_date", "last_update")
    search_fields = ('title', "name")




@admin.register(Discounts)
class DiscountsAdmin(ImportExportModelAdmin):
    list_display = ('id', "name", 'price', 'discount_price', "title", "image", "created_date", "last_update")
    search_fields = ('title', "name")
    # ordering = ("id")  #id buyicha tartiblab chiqaradi



@admin.register(Masters)
class MastersAdmin(ImportExportModelAdmin):
    list_display = ('id', "first_name", "last_name", "title", "slug", "image", "telegram_link", "static", "instagram_link", "imail_link", "created_date", "last_update")
    search_fields = ('id', "first_name")

@admin.register(Clients)
class ClientsAdmin(ImportExportModelAdmin):
    list_display = ('id', "first_name", "last_name", "title", "image", 'created_date', 'last_update', 'message',)
    search_fields = ('id', "firs_nmae")

@admin.register(Locations)
class ClientsAdmin(ImportExportModelAdmin):
    list_display = ('id', "address", "email", "iphone", 'created_date', 'last_update')
    search_fields = ('id', "address")
    # ordering = ("id")  #id buyicha tartiblab chiqaradi





