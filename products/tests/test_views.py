from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from products.tests.factories import ProductFactory


class ProductsTestClass(TestCase):

    @classmethod
    def setUpTestData(self):
        self.username = "randomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

    def setUp(self):
        self.client.login(username=self.username, password=self.password)

        self.object = ProductFactory(
            code='e3f40c7f-a65a-4419-83af-04c00d8819f8',
            price_buy=Decimal('222.68'),
            price_sell=Decimal('228.89')
        )

    def test_get_price_from_code_ok(self):
        url = reverse('retrieve-product')
        data = {'code': 'e3f40c7f-a65a-4419-83af-04c00d8819f8'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['price_buy'], '222.68')
        self.assertEqual(response.data['price_sell'], '228.89')
        self.assertEqual(str(self.object), 'Product: oficial - 222.68|228.89')

    def test_get_value_if_not_exist(self):
        url = reverse('retrieve-product')
        data = {'code': 'aaf63cb3-a22a-4419-83af-04c00d8819f8'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_price_fbad_request(self):
        url = reverse('retrieve-product')
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
