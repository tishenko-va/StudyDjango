from django.shortcuts import render
from django.views.generic import TemplateView


def main_page(request):
    return render(request, 'second_task/main.html')
def index(request):
    return render(request, 'second_task/func_template.html')

class Index2(TemplateView):
    template_name = 'second_task/class_template.html'

