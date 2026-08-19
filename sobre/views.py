from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def meus_dados(request):
    return HttpResponse("<h1>Nome: Vinicius <\h1>\nCurso: S.I \nDjango é divertido!")