"""
Testes melhorados para City usando factories.
Mantém compatibilidade com testes existentes.
"""
from django.test import TestCase
from django.core.exceptions import ValidationError
from main.models import City

# Tente importar factory, se não existir use dados manuais
try:
    from main.tests.factories import CityFactory, CityTraitFactory
    FACTORY_AVAILABLE = True
except ImportError:
    FACTORY_AVAILABLE = False


class CityModelImprovedTest(TestCase):
    """
    Testes melhorados para City.
    Usa factories quando disponível, senão usa dados manuais.
    """

    def setUp(self):
        """Setup para cada teste."""
        self.valid_city_data = {
            'city_name': 'São Paulo',
            'short_name': 'SP'
        }

    def test_city_creation_basic(self):
        """Testa criação básica compatível com teste original."""
        city = City.objects.create(**self.valid_city_data)
        
        self.assertIsNotNone(city.id)
        self.assertEqual(city.city_name, 'São Paulo')
        self.assertEqual(city.short_name, 'SP')

    def test_city_str_method(self):
        """Testa método __str__ - compatível com teste original."""
        city = City.objects.create(**self.valid_city_data)
        self.assertEqual(str(city), "São Paulo")

    def test_city_with_factory(self):
        """Testa criação usando factory se disponível."""
        if not FACTORY_AVAILABLE:
            self.skipTest("Factory-boy não está disponível")
        
        city = CityFactory()
        
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.city_name)
        self.assertGreaterEqual(len(city.short_name), 2)

    def test_multiple_cities_creation(self):
        """Testa criação de múltiplas cidades."""
        if FACTORY_AVAILABLE:
            cities = CityFactory.create_batch(3)
        else:
            # Fallback manual
            cities = [
                City.objects.create(city_name=f"City {i}", short_name=f"C{i}")
                for i in range(1, 4)
            ]
        
        self.assertEqual(len(cities), 3)
        self.assertEqual(City.objects.count(), 3)

    def test_city_ordering(self):
        """Testa ordenação alfabética por nome."""
        if FACTORY_AVAILABLE:
            CityFactory(city_name="Zebra City")
            CityFactory(city_name="Alpha City")
        else:
            City.objects.create(city_name="Zebra City", short_name="ZC")
            City.objects.create(city_name="Alpha City", short_name="AC")
        
        cities = list(City.objects.all())
        self.assertEqual(cities[0].city_name, "Alpha City")
        self.assertEqual(cities[1].city_name, "Zebra City")

    def test_city_update(self):
        """Testa atualização de cidade."""
        city = City.objects.create(**self.valid_city_data)
        
        city.city_name = "São Paulo - Capital"
        city.save()
        
        updated_city = City.objects.get(id=city.id)
        self.assertEqual(updated_city.city_name, "São Paulo - Capital")

    def test_city_delete(self):
        """Testa deleção de cidade."""
        city = City.objects.create(**self.valid_city_data)
        city_id = city.id
        
        city.delete()
        
        with self.assertRaises(City.DoesNotExist):
            City.objects.get(id=city_id)

    def test_city_empty_fields(self):
        """Testa campos obrigatórios."""
        with self.assertRaises(Exception):  # IntegrityError ou ValidationError
            City.objects.create(city_name="", short_name="")

    def test_city_max_length(self):
        """Testa limites de tamanho dos campos."""
        long_name = "A" * 101  # Excede max_length de 100
        city = City(city_name=long_name, short_name="TEST")
        
        with self.assertRaises(ValidationError):
            city.full_clean()

    def test_brazilian_cities_trait(self):
        """Testa factory com trait brasileira se disponível."""
        if not FACTORY_AVAILABLE:
            self.skipTest("Factory-boy não está disponível")
        
        city = CityTraitFactory(brazilian=True)
        
        self.assertIsNotNone(city.city_name)
        self.assertGreaterEqual(len(city.short_name), 2)
