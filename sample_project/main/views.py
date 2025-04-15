# sample_project/main/views.py

from rest_framework import generics
from .models import City
from .serializers import CitySerializer


class CityListCreateAPIView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    import ipdb

    # ipdb.set_trace()


class CityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
