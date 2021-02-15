from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


data = {
    'userName': 'admin'
}


# Create your views here.
def home(request):
    context = {
        'userName': 'admin'
    }
    return render(request, 'pixel_admin/pixel_html/dashboard.html', context)
