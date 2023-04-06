from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
class ProductsView(APIView):

    def post(self, request):
        # import ipdb; ipdb.set_trace()
        if not request.data.get('code'):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        code = request.data.get('code')
        
        try:
            product = Product.objects.get(code=code)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)

        return Response(data=serializer.data)