from django.urls import path
from .views import main_page, cart_page, shop_page

urlpatterns = [
    path('task3/', main_page),
    path('task3_shop/', shop_page),
    path('task3_cart/', cart_page),
]
