from django.shortcuts import render
#from .models import 
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def AboutMe(request):
    return render(request, "signup.html")

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")