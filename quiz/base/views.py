from django.http import HttpResponse # importo o modulo HttpResponse que me da a resposta no meu mapeamento.
from django.shortcuts import render

# Create your views here.


def home(request): #como funciona a requisução ?
    return HttpResponse('Olá mundo!')