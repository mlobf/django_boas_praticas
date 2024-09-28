# sample_project/main/serializers.py

from rest_framework import serializers
from .models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
