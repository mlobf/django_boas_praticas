from django.contrib import admin
from .models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'short_name')
    search_fields = ('city_name', 'short_name')
    ordering = ('city_name',)
