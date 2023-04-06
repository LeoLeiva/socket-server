from django.conf.urls import url

from products.views import ProductsView


urlpatterns = [
    url(
        r'api/product/$',
        ProductsView.as_view(),
        name="retrieve-product"
    ),
]