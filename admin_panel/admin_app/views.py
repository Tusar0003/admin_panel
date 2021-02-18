from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


context = {'userName': 'admin'}


def home(request):
    return render(request, 'pixel_admin/pixel_html/dashboard.html', context)


def profile(request):
    return render(request, 'pixel_admin/pixel_html/profile.html', context)


def basic_table(request):
    return render(request, 'pixel_admin/pixel_html/basic-table.html', context)


def blank_page(request):
    return render(request, 'pixel_admin/pixel_html/blank.html', context)


def error_page(request):
    return render(request, 'pixel_admin/pixel_html/404.html', context)
