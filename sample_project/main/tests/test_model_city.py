from django.test import TestCase
from main.models import City


class CityModelTwoTest(TestCase):
    fixtures = ['main/tests/fixtures/cities.json']

    def test_all_cities(self):
        """Testa de o total de cidades contidas no mock
        cities.json é o esperado em teste"""

        len_cities = City.objects.all()
        self.assertEqual(len(len_cities), 12)

    def test_read_city(self):
        city = City.objects.get(city_name='Belo Horizonte')
        self.assertEqual(city.short_name, 'BH')

    def test_update_city(self):
        city = City.objects.get(city_name='Belo Horizonte')
        city.short_name = 'bh'
        city.save()
        updated_city = City.objects.get(pk=city.pk)
        self.assertEqual(updated_city.short_name, 'bh')
        updated_city.short_name = 'BH'
        city.save()

    def test_delete_city(self):
        city = City.objects.get(city_name='Belo Horizonte')
        city_id = city.pk
        city.delete()
        with self.assertRaises(City.DoesNotExist):
            City.objects.get(pk=city_id)

    def test_create_city(self):
        city = City.objects.create(city_name='Piracicaba', short_name='PIRA')
        self.assertEqual(city.city_name, 'Piracicaba')
        self.assertEqual(city.short_name, 'PIRA')


