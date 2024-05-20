from django.contrib import admin
from .models import Products, Services
from import_export.admin import ImportExportModelAdmin

@admin.register(Products)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', "title", "name", "image", "created_date", "last_update")
    search_fields = ('id', "title")

@admin.register(Services)
class ServicesAdmin(ImportExportModelAdmin):
    list_display = ('id', "title", "image", 'created_date')
    search_fields = ('id', "title")

# admin.site.register(Products)
# admin.site.register(Services)

# Register your models here.
