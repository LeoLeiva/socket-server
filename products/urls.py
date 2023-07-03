from django.urls import re_path

from products.views import ProductsView


urlpatterns = [
    re_path(
        r'api/product/$',
        ProductsView.as_view(),
        name="retrieve-product"
    ),
]