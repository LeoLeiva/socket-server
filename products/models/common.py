# -*- coding: utf-8 -*-
import uuid

from django.db import models

from products.constants import DenominationConstants

from .base import TimeStampedModel

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
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    price_buy = models.DecimalField(
        max_digits=30, decimal_places=2,
        verbose_name=("Precio de compra"), default=0
    )
    price_sell = models.DecimalField(
        max_digits=30, decimal_places=2,
        verbose_name=("Precio de venta"), default=0
    )
    description = models.CharField(max_length=250, null=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return "{}: {} - {}|{}".format(
            self.__class__.__name__,
            self.denomination,
            self.price_buy,
            self.price_sell
        )
