from django.shortcuts import render


def login(request):
    return render(request, 'login_form/login/login.html')


def registration(request):
    return render(request, 'login_form/login/registration.html')
