from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login-home'),
    path('registration/', views.registration, name='login-registration')
]
