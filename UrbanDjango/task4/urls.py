from django.urls import path
from .views import main_page, cart_page, shop_page


urlpatterns = [
    path('', main_page),
    path('shop/', shop_page),
    path('cart/', cart_page),
]