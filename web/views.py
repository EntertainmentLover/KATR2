from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html')

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def home(request):
    return render(request, 'users/home.html')