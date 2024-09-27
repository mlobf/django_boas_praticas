from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    """
    Model City relation Address
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=80, verbose_name=_('Name'), db_index=True)
    short_name = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('Short Name'))

    class Meta:
        ordering = ['name']
        verbose_name = _('City')
        verbose_name_plural = _('Cities')


class Address(models.Model):
    """
    Model Address
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=80, verbose_name=_('Name'), db_index=True)
    short_name = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('Short Name'))
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
