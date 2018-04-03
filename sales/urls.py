from django.conf.urls import url

from .views import (list_sale, create_sale, edit_sale, delete_sale, get_products_api_view,
    get_product_fixed_price)

urlpatterns = [
    url(r'^view/(?P<slug>[\w-]+)/$', list_sale, name='home'),
    url(r'^create/$', create_sale, name='create'),
    # url(r'^create/(?P<slug>[\w-]+)/$', create_sale, name='create'),
    url(r'^edit/(?P<pk>\d+)/$', edit_sale, name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', delete_sale, name='delete'),
    url(r'^get-products/(?P<pk>\d+)/$', get_products_api_view, name='get_products'),
    url(r'^get-product-price/(?P<pk>\d+)/$', get_product_fixed_price, name='get_product_rate'),
]