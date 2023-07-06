import factory
from faker import Factory

from products.constants import DenominationConstants
from products.models import Product

faker = Factory.create()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    denomination = DenominationConstants.OFICIAL
    price_buy = factory.LazyAttribute(
        lambda _: faker.numerify(
            text='#####.##'))
    price_sell = factory.LazyAttribute(
        lambda _: faker.numerify(text='#####.##'))
