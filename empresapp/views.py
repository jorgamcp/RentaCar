from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,template_name='index.html')

def tarifas(request):
    return render(request,template_name='tarifas.html')

def reservar(request):
    return render(request,template_name="reserva.html")
def tos(request):
    return render(request,template_name="tos.html")

def about(request):
    return render(request,template_name='about.html')