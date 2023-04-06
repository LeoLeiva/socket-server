from __future__ import absolute_import
from celery import Celery
from decimal import Decimal
import logging
import requests
from products.constants import TWOPLACES
from products.models import Product


app = Celery('products')
logger = logging.getLogger(__name__)

@app.task()
def update_values():
    '''Update the price of all products'''
    response = requests.get('http://api.bluelytics.com.ar/v2/latest').json()
    for product in Product.objects.all():
        value_buy = Decimal(response[product.denomination]['value_buy']).quantize(TWOPLACES)
        value_sell = Decimal(response[product.denomination]['value_sell']).quantize(TWOPLACES)
        product.price_buy = value_buy
        product.price_sell = value_sell
        product.save()
        logger.info('Se actualizo el precio del %s. Compra: %s - Venta: %s' % (
            product.get_denomination_display(),
            str(value_buy),
            str(value_sell)
        ))
