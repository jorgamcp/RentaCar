from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import logout as django_logout
from django import forms
from django.contrib.auth import authenticate


from .models import User
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63,widget=forms.PasswordInput)

user = User()    
# Create your views here.
def index(request):
    
    return render(request,'index.html',{'user':user})

def tarifas(request):
    return render(request,template_name='tarifas.html')

def reservar(request):
    return render(request,template_name="reserva.html")
def tos(request):
    return render(request,template_name="tos.html")

def about(request):
    return render(request,template_name='about.html')

def login(request):
   return render(request,template_name='login.html')

def logout(request):
    django_logout(request)
    return redirect('/')