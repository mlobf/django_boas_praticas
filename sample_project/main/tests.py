from django.test import TestCase
from .models import City
import uuid


class CityModelTest(TestCase):
    fixtures = ['cities.json']

    def test_read_city(self):
        city = City.objects.get(city_name='São Paulo')
        self.assertEqual(city.short_name, 'SP')

    def test_update_city(self):
        city = City.objects.get(city_name='Rio de Janeiro')
        city.short_name = 'RIO'
        city.save()
        updated_city = City.objects.get(pk=city.pk)
        self.assertEqual(updated_city.short_name, 'RIO')

    def test_delete_city(self):
        city = City.objects.get(city_name='São Paulo')
        city_id = city.pk
        city.delete()
        with self.assertRaises(City.DoesNotExist):
            City.objects.get(pk=city_id)

    def test_create_city(self):
        city = City.objects.create(
            city_name='Curitiba',
            short_name='CTBA'
        )
        self.assertEqual(city.city_name, 'Curitiba')
        self.assertEqual(city.short_name, 'CTBA')
        self.assertIsInstance(city.pk, uuid.UUID)
