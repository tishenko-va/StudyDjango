from django.shortcuts import render

def main_page(request):
    return render(request, 'forth_task/main_page.html')

def shop_page(request):
    products = ['Гречка', 'Рис', 'Макароны']
    context = {
        'list': products
    }

    return render(request, 'forth_task/shop_page.html', context)

def cart_page(request):
    return render(request, 'forth_task/cart_page.html')
