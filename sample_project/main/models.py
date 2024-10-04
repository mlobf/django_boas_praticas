from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    """
    Model City relation Address
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    city_name = models.CharField(max_length=80, verbose_name=_('Name'), db_index=True)
    short_name = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('Short Name'))

    class Meta:
        ordering = ['city_name']
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return f'{self.id}+{self.city_name}+{self.short_name}'

    def __repre__(self):
        return f'{self.id}+{self.city_name}+{self.short_name}'


"""
Simular um comportamento basico para o sistema de jogos para simular uma melhor implementacao.

Model Cassino
Model Game
Model Operator
Model Currency
Model User
Model Igs

"""
