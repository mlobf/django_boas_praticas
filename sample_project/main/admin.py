from django.contrib import admin
from .models import City, Address


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    search_fields = ('name', 'short_name')
    ordering = ('name',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'name', 'short_name')
    search_fields = ('city__name', 'name', 'short_name')
    list_filter = ('city', 'name')


