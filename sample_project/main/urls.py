# sample_project/main/urls.py

from django.urls import path
from .views import CityListCreateAPIView, CityRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('cities/', CityListCreateAPIView.as_view(), name='city-list-create'),
    path('cities/<uuid:pk>/', CityRetrieveUpdateDestroyAPIView.as_view(), name='city-detail'),
]
