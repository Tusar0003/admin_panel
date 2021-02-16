from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin-home'),
    path('profile/', views.profile, name='admin-profile'),
    path('basic-table/', views.basic_table, name='admin-basic-table'),
]
