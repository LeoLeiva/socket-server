# -*- coding: utf-8 -*-
from decimal import Decimal
import uuid

from django.db import models
from django.utils.translation import ugettext as _

from .base import TimeStampedModel
from products.constants import DenominationConstants


__all__ = [
    'Product',
]

class Product(TimeStampedModel):

    id = models.AutoField(primary_key=True)
    denomination = models.CharField(
        default=DenominationConstants.OFICIAL,
        max_length=50,
        choices=DenominationConstants.CHOICES,
        null=True,
        blank=True
    )
    code = models.UUIDField(
        default = uuid.uuid4,
        editable = False,
        unique=True
    )
    price_buy = models.DecimalField(
        max_digits=30, decimal_places=2,
        verbose_name=_("Precio de compra"), default=0
    )
    price_sell = models.DecimalField(
        max_digits=30, decimal_places=2,
        verbose_name=_("Precio de venta"), default=0
    )
    description = models.CharField(max_length=250, null=True)
    
    class Meta:
        ordering = ["-id"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"