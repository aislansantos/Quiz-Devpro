from django.shortcuts import render

# Create your views here.


def home(request): #como funciona a requisução/request ?
    return render(request, 'base/home.html')
