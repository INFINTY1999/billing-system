from django.urls import re_path, include, path
from apps.products.views import index_page, cart_page

urlpatterns = [
    path("", index_page, name="index_page"),
    path("/cart/", cart_page, name="cart_page"),
]
