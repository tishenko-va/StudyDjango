from django.urls import path
from .views import main_page, index, Index2

urlpatterns = [
    path('task2/', main_page),
    path('index/', index),
    path('index2/', Index2.as_view()),
]
