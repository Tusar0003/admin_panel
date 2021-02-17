from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


data = {
    'userName': 'admin'
}


def home(request):
    context = {
        'userName': 'admin'
    }
    return render(request, 'pixel_admin/pixel_html/dashboard.html', context)


def profile(request):
    return render(request, 'pixel_admin/pixel_html/profile.html')


def basic_table(request):
    return render(request, 'pixel_admin/pixel_html/basic-table.html')


def blank_page(request):
    return render(request, 'pixel_admin/pixel_html/blank.html')


def error_page(request):
    return render(request, 'pixel_admin/pixel_html/404.html')
