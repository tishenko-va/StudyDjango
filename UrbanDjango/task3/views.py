from django.shortcuts import render
from django.views.generic import TemplateView

def main_page(request):
    return render(request, 'third_task/main_page.html')

def shop_page(request):
    items = {
        'item1': 'Гречка',
        'item2': 'Рис',
        'item3': 'Макароны'
    }
    return render(request, 'third_task/shop_page.html', {'items': items})

def cart_page(request):
    return render(request, 'third_task/cart_page.html')