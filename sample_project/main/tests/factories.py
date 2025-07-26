"""
Factory classes for creating test data.
Substitui fixtures estáticas por dados dinâmicos.
"""
import factory
from factory import django, Faker
from main.models import City


class CityFactory(django.DjangoModelFactory):
    """Factory para criar instâncias de City nos testes."""
    
    class Meta:
        model = City
    
    city_name = Faker('city')
    short_name = factory.LazyAttribute(
        lambda obj: obj.city_name[:3].upper() if obj.city_name else 'XXX'
    )

    @factory.post_generation
    def ensure_valid_short_name(obj, create, extracted, **kwargs):
        """Garante que short_name seja válido."""
        if len(obj.short_name) < 2:
            obj.short_name = obj.short_name + 'X' * (2 - len(obj.short_name))
        if len(obj.short_name) > 10:
            obj.short_name = obj.short_name[:10]
        if create:
            obj.save()


class CityTraitFactory(CityFactory):
    """Factory com traits para casos específicos."""
    
    class Meta:
        model = City
    
    class Params:
        brazilian = factory.Trait(
            city_name=factory.Faker('city', locale='pt_BR'),
            short_name=factory.LazyAttribute(lambda o: o.city_name[:3].upper())
        )
        
        american = factory.Trait(
            city_name=factory.Faker('city', locale='en_US'),
            short_name=factory.LazyAttribute(lambda o: o.city_name[:3].upper())
        )
