from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ola_mundo(request):
    return HttpResponse("<h1>Olá, Django!<\h1>")